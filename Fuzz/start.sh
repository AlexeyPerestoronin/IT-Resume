# create virtual environment for python if not created
if [ ! -d .venv ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt
pip install -e "../../CommandScript"

invoke get-info
invoke --list