**Generator load for server**
-

**Create venv**	

py -m venv venv

**Activate venv**

venv\Scripta\activate

**Install**

pip install -r requirements.txt

**Create** file **"my.py"**, where you define your URL 

For example:

IP_ADDRESS = "my_server_ip"
PORT = "5000"
MY_URL = f"http://{IP_ADDRESS}:{PORT}/test"
