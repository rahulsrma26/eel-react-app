EEL REACT VITE Example
=======================

This is an example of EEL app that uses react for UI and vite for build.



## How to setup

Clone (or fork and clone) this repo and change dir.

```sh
git clone https://github.com/rahulsrma26/eel-react-app.git
cd eel-react-app
```

Install packages using yarn or npm.

```sh
npm install
```

Create environment and install requirements for python.

```sh
conda create -n appenv python=3.9 pip
conda activate appenv
pip install -r requirements.txt
```

---

## How to develop

To run the example in dev environment first run front end.

```sh
npm run dev
```

Then run backend in a separate terminal.
```sh
python main.py --dev
```

---

## How to build executable

To build and executable first build static files.

```sh
npm run build
```

Then build using pyinstaller.
```sh
python -m eel main.py dist --onefile --noconsole --name eel-react-app
```
