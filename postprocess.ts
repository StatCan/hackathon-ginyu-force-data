// Helper library written for useful postprocessing tasks with Flat Data
// Has helper functions for manipulating csv, txt, json, excel, zip, and image files
import { xlsx, readXLSX, writeCSV } from "https://deno.land/x/flat@0.0.11/mod.ts";

// Get the downloaded_filename as the first argument
const inputFilename = Deno.args[0];
const outputFilename = inputFilename.replace(".xlsx", ".csv");

// read about what the xlsx library can do here: https://github.com/SheetJS/sheetjs

const workbook = await readXLSX(inputFilename);
const sheetData = workbook.Sheets[workbook.SheetNames[0]];
const csvString = await xlsx.utils.sheet_to_csv(sheetData); // can use to_json, to_txt, to_html, to_formulae

// write to csv
await writeCSV(outputFilename, csvString);

// unlink the file
const unlink = Deno.run({
    cmd: ['rm', inputFilename],
});
await unlink.status();


// install requirements with pip
const pip_install = Deno.run({
    cmd: ['python', '-m', 'pip', 'install', '-r', 'requirements.txt'],
});

await pip_install.status();

console.log("pip install successful");

// Forwards the execution to the python script
const py_run = Deno.run({
    cmd: ['python', './postprocess.py'].concat(Deno.args),
});

await py_run.status();

console.log("python script successful?");
