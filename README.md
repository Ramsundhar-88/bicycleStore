### bicycle

this project will implement ERPNext for a Bicycle Store to manage daily operations such as Sales, Purchase, Inventory, Customer Management, Invoicing, and operational reporting. In addition to standard ERPNext modules, a Custom App will be developed to enforce discount control, approval rules, and sales automation, ensuring faster processing and reduced manual errors.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app bicycle_store
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/bicycle_store
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
