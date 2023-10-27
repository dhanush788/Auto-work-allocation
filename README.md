# Auto Work Allocation

The **Auto Work Allocation** project is a system designed to automate the task of assigning work to individuals within an organization based on various factors, including their skills, previous day's performance data, workload, and other relevant criteria. The primary goal of this project is to optimize the allocation of tasks and responsibilities to maximize efficiency and productivity while ensuring that each person is assigned tasks that align with their expertise and availability.

## Key Features and Components

## Task Management System Features:

1. **Visual Task Management**: Utilizes task boards and task cards to provide a visual representation of work items, making it easy to categorize and track tasks.

2. **Task Assignment and Details**: Allows task assignment to individuals and provides detailed task information, including descriptions and due dates.

3. **Task Progress Tracking and Collaboration**: Supports progress tracking as tasks move through stages and enables collaboration through task comments.

4. **Task Categorization and Filtering**: Users can label and tag tasks for categorization and efficient filtering.

5. **Workload Management**: Analyzes current employee workloads to ensure a balanced distribution of tasks, preventing overburdening.

6. **Automated Reminders and Notifications**: Sends automated reminders for task deadlines and keeps users informed through notifications.

7. **User Permissions and Data Security**: Implements role-based permissions for data security and privacy.

8. **Real-time Updates and Reporting**: Provides real-time updates on the task board and offers reporting and analytics tools for performance assessment.

9. **User-Friendly Interface**: Designed for easy interaction, making task management seamless for both employees and managers.

## Work Allocation System with Skill Matching Features:

1. **Skill-Based Task Assignment**: Matches tasks with employees based on their skills and qualifications for optimal task allocation.

2. **Data-Driven Allocation**: Considers performance data from the previous day to identify patterns and allocate tasks effectively.

3. **Workload Optimization**: Ensures a fair distribution of tasks by considering employees' current workloads.

4. **Task Prioritization**: Prioritizes tasks based on importance, deadlines, and other factors for efficient completion.

5. **Automated Scheduling and Dynamic Adjustments**: Includes automated scheduling while making real-time adjustments for urgent tasks or changing circumstances.

6. **Data-Driven Decision-Making**: Provides reporting and analytics tools for managers to make informed work allocation decisions.

7. **User-Friendly Interface for Requests**: Offers a user-friendly interface for employees and managers to interact with the system and request task changes.

## Dependencies

1. [python](https://www.python.org/downloads/)
2. [npm](https://www.npmjs.com/)

```
Python dependencies:
Package            Version
------------------ ----------------------------------
annotated-types    0.5.0
apparmor           3.1.6
arandr             0.1.11
attrs              22.2.0
auto-cpufreq       1.9.7
autocommand        2.2.2
CacheControl       0.13.1
cffi               1.15.1
chardet            5.2.0
click              8.1.7
cryptography       41.0.4
dbus-python        1.3.2
distro             1.8.0
docopt             0.6.2
fastjsonschema     2.18.1
feedparser         6.0.10
filelock           3.12.4
html2text          2020.1.16
idna               3.4
inflect            7.0.0
informant          0.4.6
jaraco.context     4.3.0
jaraco.functools   3.9.0
jaraco.text        3.11.1
LibAppArmor        3.1.6
lockfile           0.12.2
more-itertools     10.1.0
msgpack            1.0.5
optimus-manager    1.5
ordered-set        4.1.0
packaging          23.1
pip                23.2.1
platformdirs       3.11.0
ply                3.11
psutil             5.9.5
pycairo            1.24.0
pycparser          2.21
pydantic           2.3.0
pydantic_core      2.6.3
PyGObject          3.46.0
python-dateutil    2.8.2
Reflector          2023.6.28.0.36.1
requests           2.28.2
setuptools         68.0.0
sgmllib3k          1.0.0
six                1.16.0
tomli              2.0.1
trove-classifiers  2023.9.22
typing_extensions  4.8.0
urllib3            1.26.15
validate-pyproject 0.13.post1.dev0+gb752273.d20230520
wheel              0.40.0
```

You can either install the python dependencies on your pc, or create a virtual environment:

```bash
python3 -m venv <env_name>

# Activate virtual environment
source <env_name>/bin/activate

# Upgrade pip
pip install --upgrade pip

pip install scikit-learn
pip install spacy
pip install $(spacy info en_core_web_sm --url)

# Deactivate virtual environment ( after use )
deactivate
```

## Usage:
<br>

By automating the work allocation process, this project aims to streamline operations, reduce the potential for human error, increase employee satisfaction by assigning them tasks that match their skills and preferences, and ultimately enhance the overall productivity and efficiency of the organization. This type of system is particularly valuable in settings where there is a high volume of task allocation or where tasks are highly specialized and require specific skills or knowledge.


## Instructions

To set up and run this project, follow these steps:

1. Make sure all [dependencies](https://github.com/dhanush788/Auto-work-allocation#dependencies) are met

2. Change current directory to root directory of project

3. Install project dependencies using npm:

   ```bash
   npm install
   ```

4. Export the NODE_OPTIONS environment variable to use the legacy OpenSSL provider:
   ```bash
    export NODE_OPTIONS=--openssl-legacy-provider
   ```

5. npm start
   ```bash
    npm start
   ```


