# Weather Demo

A small Python command-line project that fetches a text weather report from
[wttr.in](https://wttr.in/) and prints it in the terminal. The project also
demonstrates how to load configuration from environment variables with
`python-dotenv`.

## Features

- Loads local configuration from a `.env` file when one is available.
- Uses `Phnom Penh` as the default value of `CITY`.
- Requests a plain-text weather report from `wttr.in`.
- Prints the configured city label followed by the service response.

> [!NOTE]
> In the current implementation, `CITY` controls the heading printed by the
> application. The request itself is sent to the wttr.in root endpoint, so the
> weather service determines the report location independently.

## Requirements

- Python 3.9 or newer
- An internet connection for reaching `https://wttr.in`

The Python packages used by the project are pinned in `requirements.txt`.

## Getting started

### 1. Clone the repository

```bash
git clone <repository-url>
cd weather-demo
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the city label (optional)

Create a `.env` file in the project root:

```dotenv
CITY=Phnom Penh
```

If `CITY` is omitted, the application uses `Phnom Penh` by default. You can
also provide the variable directly when starting the application:

```bash
CITY="London" python app.py
```

### 5. Run the application

```bash
python app.py
```

The terminal output begins with the configured city heading and is followed by
the weather report returned by wttr.in.

## Project structure

```text
weather-demo/
├── app.py            # Loads configuration and retrieves the weather report
├── requirements.txt  # Pinned Python dependencies
└── README.md         # Project documentation
```

## Configuration

| Variable | Required | Default | Purpose |
| --- | --- | --- | --- |
| `CITY` | No | `Phnom Penh` | Sets the city name displayed in the output heading. |

Do not commit `.env` files if you later add secrets or other sensitive values
to them.

## Troubleshooting

- **Dependency import errors:** Make sure the virtual environment is active,
  then run `python -m pip install -r requirements.txt` again.
- **Connection errors:** Confirm that the machine can access `https://wttr.in`
  and that a proxy or firewall is not blocking the request.
- **Unexpected location in the report:** The current request does not pass
  `CITY` to wttr.in; the variable only changes the printed heading.

## Acknowledgements

Weather data and terminal formatting are provided by
[wttr.in](https://wttr.in/).
