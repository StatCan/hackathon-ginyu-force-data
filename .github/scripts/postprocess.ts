// `xlsx` is SheetJS: https://github.com/SheetJS/sheetjs
import {
  readXLSX,
  writeCSV,
  xlsx,
} from "https://deno.land/x/flat@0.0.11/mod.ts";
import { datetime } from "https://deno.land/x/ptera/mod.ts";

const col = Object.freeze({
  id: "estma_id",
  entity: "entity",
  jurisdiction: "jurisdiction",
  period_start: "period_start_date",
  period_end: "period_end_date",
  reporting_cycle: "reporting_cycle",
  country: "country",
  payee_project_name: "payee_project_name",
  payee_or_project: "payee_or_project",
  payment_category: "payment_category",
  amount: "amount_reported_cad",
  link: "web_link",
  type_of_report: "type_of_report",
});
const oldCol: Partial<typeof col> = Object.freeze({
  reporting_cycle: "reporting_cylce",
  link: "web_Link",
});

const EXCEL_REF_DATE = datetime("1899-12-30");
function excelDateToIso(excelInt: number) {
  return EXCEL_REF_DATE.add({ day: excelInt }).toISODate();
}

// Get the downloaded_filename as the first argument
const inputFilename = Deno.args[0];
const outputFilename = inputFilename.replace(".xlsx", ".csv");

const workbook = await readXLSX(inputFilename);
const sheetData = workbook.Sheets[workbook.SheetNames[0]];
const rows: any = xlsx.utils.sheet_to_json(sheetData);

// Do processing
for (const row of rows) {
  // Rename columns
  for (const [key, oldName] of Object.entries(oldCol)) {
    if (row.hasOwnProperty(oldName)) {
      row[col[key as keyof typeof col]] = row[oldName];
      delete row[oldName];
    }
  }

  // Convert Excel date integers to ISO strings
  row[col.period_start] = excelDateToIso(row[col.period_start]);
  row[col.period_end] = excelDateToIso(row[col.period_end]);
}

await writeCSV(outputFilename, rows);

const pip_install = Deno.run({
  cmd: [
    "python",
    "-m",
    "pip",
    "install",
    "-r",
    ".github/scripts/requirements.txt",
  ],
});
await pip_install.status();

const pyRun = Deno.run({
  cmd: ["python", "./.github/scripts/postprocess.py"].concat(Deno.args),
});
await pyRun.status();

Deno.removeSync(inputFilename);
