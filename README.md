dropzone
========

Geo-centric content sharing 

### initializing database

Make sure to create local postgres database named 'dropzone'. 

Initialize Alembic for migrations:
<pre><code>$ python manage.py db init</code></pre>

### running migrations

Create migration:
<pre><code>$ python manage.py db migrate</code></pre>

Apply upgrades to database:
<pre><code>$ python manage.py db upgrade</code></pre>

### running the app

Install required dependencies:
<pre><code>$ pip install -r requirements.txt</code></pre>

Run the app:
<pre><code>$ python run.py</code></pre>
