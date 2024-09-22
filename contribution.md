# Contributing

If you wish to contribute to this repository, feel free to fork the repository and submit a
pull request. We welcome any contribution; small or big, code or no-code.

## Setup

To get ready to work on the codebase, please do the following:

1. Fork and clone the repository, and make sure you're on the **main** branch
```
git clone https://github.com/[your-username]/collescope.git
cd collescope
```
2. Setup a virtual environment to avoid conflicts with other projects and to manage dependencies

``` bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On macOS/Linux
source env/bin/activate

# On Windows
env\Scripts\activate

```
3. Install all required dependencies from `requirements.txt
```bash
pip install -r requirements.txt
```

4. Running the application
```
uvicorn app.main:app --reload
```

## Steps for Adding a College Entry

- Open the file `app/colleges.json`.
  
- Add a new entry at the end of the JSON array, following this structure:

  ```json
  {
    "id": 3,
    "name": "College Name",
    "location": "Location of the College",
    "website": "https://college-website.com"
  }
id: This should be a unique number. Increment the highest existing id by 1.

name: The full name of the college.

location: The location or address of the college.

website: The official website of the college (ensure it starts with https:// for proper formatting).

- Save the changes and do the steps of contrubuting as instructed.

## Contributing

1. Create a new branch for your information or feature
```
git checkout -b <mybranch>
```
2. Add the changed file
```
git add .
```
3. Commit your changes
```
git commit -m "commit message"
```
4. Push to the branch
```
git push origin <mybranch>
```
5. Submit a pull request
