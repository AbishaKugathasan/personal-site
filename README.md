# Production Engineering - Portfolio Site
***Note: This is an imported repo from my MLH project, so I can run it on another clouding site
Please visit https://github.com/AbishaKugathasan/MLHFellowshipProject for more details of the site and features***

My personal portfolio website that showcases my projects, experience, hobbies and education.

## Visuals
<img width="500" alt="Screen Shot 2022-07-15 at 9 17 48 PM" src="https://user-images.githubusercontent.com/77181669/179336802-935db26c-9531-4b6c-91df-0456c706a65a.png">

<img width="500" alt="Screen Shot 2022-07-15 at 9 18 27 PM" src="https://user-images.githubusercontent.com/77181669/179336822-e763eaf0-11cc-4847-9977-f5751ff34a71.png">


## Technologies Used :computer:
- HTML & CSS for the frontend
- Python, Flask, & Jinja to make use of reusable templates and route to different URLs
- Openweathermap API 
- NASA API 

## Special Features of the Site 
## Weather :sunny:
- Displays weather information and an approporiate picture which correlates to the weather displayed. Works with daytime and nighttime. 

## NASA POTD :telescope:
- Displays NASA's picture of the day in the about me section - which is recieved from using NASA's API. 

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
