# Finding Exchange Rates for International Sales

## Overview

This project analyzes international sales data for the DataGadgets webshop by integrating real-time exchange rates to convert transactions into USD. Initially focused on the US market, the business has expanded to the UK and Europe, necessitating currency conversion for EUR and GBP transactions. The project demonstrates working with financial APIs, data manipulation, and currency conversion at scale.

## Project Structure

```bash
finding_exchange_rates/
├── data/
│   ├── orders-2024-01-21.csv   # Raw sales transactions data
├── notebook.ipynb              # Jupyter notebook for project development
├── requirements.txt            # Project dependencies
└── README.md                  # Project documentation
```

## Features

- Fetch real-time exchange rates from VAT Comply rates API
- Process international sales transactions from multiple currencies
- Convert EUR and GBP transactions to USD
- Calculate total sales volume in USD
- Cache exchange rate data for better performance

## Prerequisites

- Python 3.7+
- Access to VAT Comply rates API
- Pandas for data manipulation
- Requests for API calls

## Installation

1. Clone this repository:

    ```bash
    git clone <repository-url>
    cd finding-exchange-rates
    ```

2. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your sales data in CSV format in the `data` directory
2. Run the analysis script:

    ```bash
    python src/sales_analysis.py
    ```

## Data Format

The input CSV should include these columns:

- `amount`: Sale amount in original currency
- `currency`: Three-letter currency code (USD, EUR, GBP)

The script will add:

- `exchange_rate`: The conversion rate to USD
- `amount_usd`: The sale amount converted to USD

Example output:

```bash
   amount currency  exchange_rate  amount_usd
0   43.75      EUR      0.918527   40.185542
1  385.50      GBP      0.788326  303.899490
2  495.50      GBP      0.788326  390.615298
3  117.99      GBP      0.788326   93.014529
4  624.00      USD      1.000000  624.000000
```

## API Integration

The project uses the VAT Comply rates API (<https://www.vatcomply.com/documentation#rates>) to fetch current exchange rates. The API endpoint accepts parameters for:

- `base`: Base currency (USD in our case)
- `date`: Date for exchange rates

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
