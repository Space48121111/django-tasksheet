=====
Task
=====

Task is a Django app to conduct web-based task.
For each room, guests can choose between a fixed number of rates.

Detailed documentation is in the 'docs' directory.

Quick start
-----------
1. Add 'task' to your INSTALLED_APPS setting like this:
    INSTALLED_APPS = [
    ...
    'task',
    ]

2. Include the task URLconf in your project urls.py like this:
    path('task/', include('task.urls')),

3. Run ``python3 manage.py migrate`` to create the task models.

4. Start the development server and visit
    http://127.0.0.1:8000/admin/
    to create a task(you'll need the Admin app enabled).

5. Visit
    http://127.0.0.1:8000/ or
    http://127.0.0.1:8000/task/
    to participate in the task.





----------------
Happy coding. :)
