_⚠ This repository is for the purpose of a hackathon. Please **do not** rely on
its contents or treat it as an official data source._

# ESTMA Open Data Repository

> **🛈 Just looking for the data?**
>
> It's all in `estma-payments.csv` at the root of this repository. Have fun! 🚀

The Extractive Sector Transparency Measures Act helps the Government of Canada
deter corruption in the extractive sector. Extractive entities — oil, gas, and
mining businesses — that are active in Canada must publicly disclose certain
types of payments made to governments in Canada and abroad.

This repository contains that payments data (see `estma-payments.csv`) – as well
as some notebooks (see `notebooks/`) that analyze it – that you can use freely
for analysis.

## Using the Data

You can [**check out our website**][website] to learn about all the different
ways you can interact with and analyze the open ESTMA data.

* [Visualize and modify basic breakdowns on the website][website]
* [View and filter the microdata using GitHub Flat Viewer][flat]
* [Level up your analysis with the Advanced Analytics Workspace][aaw]

![Open ESTMA Data website][website-image]

## Why the Weird Extension on `summary.jsonfile`?

The `summary.jsonfile` is just a few lines of JSON that provide the data for high
level indicators on [the website][website]. It isn't intended for human consumption.

The GitHub Flat Viewer is hard-coded to list all JSON files in the repository, no
matter what. So we change the extension so it doesn't show up in that tool. 😎

[website]: https://statcan.github.io/hackathon-ginyu-force/index-en.html
[flat]: https://flatgithub.com/StatCan/hackathon-ginyu-force-data?filename=estma-payments.csv
[aaw]: https://analytics-platform.statcan.gc.ca/covid19
[website-image]: notebooks/.screenshots/website.png
