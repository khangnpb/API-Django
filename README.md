# API-Django
### Step 0: Create Virtual Environment
```cmd
python -m venv .venv
```
 
### Step 1: Activate env:
```cmd
./.venv/Scripts/activate
```

### Step 1.1: Install all dependencies after activate virtual environment successfully:
```cmd
pip install -r requirements.txt
```

### Step 2: Setup database
1. Run docker-compose.yaml to create Database Container.
```cmd
docker-compose up
```
2. After running, access to http://localhost:80 and log in with DB information (admin/admin)
3. In **dw** DB, import file **dw.sql**
4. Click **OK** and wait till the end of the imported process.

### Step 3: Run manage.py

#### Update database in Django (Migrations)
```cmd
python manage.py makemigrations
python manage.py migrate --fake DataWareHouse_BE
python manage.py migrate
```
![Alt text](image.png)

#### Create account to access (admin/admin)
```cmd
python manage.py createsuperuser  
```
Then, following the django instruction.

#### Run server
```cmd
python manage.py runserver
```

### Step 4: Check data:

http://localhost:8000/admin

### Step 5: Check các API:

http://localhost:8000/detail_customer/all \
http://localhost:8000/dim_customer/all \
http://localhost:8000/dim_product/all \
http://localhost:8000/dim_store/all \
http://localhost:8000/fact_ecommerce_sales/all 