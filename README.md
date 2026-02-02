# Crowdfunding Backend
Raise the Case

## Overview
A crowd-powered platform where the public helps "try" cases and mysteries in the court of public opinion. Users can review details of real cases and cast verdicts on who they believe is guilty.

## Concept
**Raise the Case** is a gamified social platform that democratises justice by allowing everyday citizens to participate in case verdicts. It serves victims who feel the justice system has failed them or cannot access it, as well as true crime enthusiasts, civil-minded citizens, investigators, and justice advocates.

## Technology Stack
- **Framework:** Django 5.1 + Django REST Framework
- **Authentication:** Token-based authentication
- **Database:** PostgreSQL (production) / SQLite (development)
- **Deployment:** Gunicorn + Whitenoise
- **CORS:** Enabled for frontend integration

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip
- Virtual environment

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd crowdfunding_backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```
   DJANGO_SECRET_KEY=your-secret-key-here
   DJANGO_DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Run migrations:**
   ```bash
   cd crowdfunding
   python manage.py migrate
   ```

6. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## API Documentation

### Authentication Endpoints

| Endpoint | Method | Purpose | Authentication |
|----------|--------|---------|-----------------|
| `/users/` | POST | Register a new user | None |
| `/api-token-auth/` | POST | Authenticate and get token | None |

### User Endpoints

| Endpoint | Method | Purpose | Authentication |
|----------|--------|---------|-----------------|
| `/users/` | GET | List all users | None |
| `/users/<id>/` | GET | Retrieve user details | None |
| `/user/profile/` | PUT | Update user profile | Required |
| `/user/profile/` | DELETE | Delete user account | Required |
| `/user/stats/` | GET | Retrieve user statistics | Required |

### Case Endpoints

| Endpoint | Method | Purpose | Authentication |
|----------|--------|---------|-----------------|
| `/cases/` | GET | Retrieve all cases | None |
| `/cases/` | POST | Create a new case | Required |
| `/cases/<id>/` | GET | Retrieve a single case | None |
| `/cases/<id>/` | PUT | Update a case | Required (case owner only) |

### Judgement Endpoints

| Endpoint | Method | Purpose | Authentication |
|----------|--------|---------|-----------------|
| `/judgements/` | GET | Retrieve all judgements | None |
| `/judgements/` | POST | Submit a new judgement | Required |
| `/judgements/<id>/` | GET | Retrieve a single judgement | None |
| `/judgements/<id>/` | PUT | Update a judgement | Required (judgement creator only) |

## Endpoint Examples

### Register a New User
```
POST /users/
Content-Type: application/json

{
  "username": "detective_jane",
  "password": "secure_password",
  "email": "jane@example.com"
}

Response: 201 Created
{
  "id": 1,
  "username": "detective_jane",
  "email": "jane@example.com"
}
```

### Authenticate (Get Token)
```
POST /api-token-auth/
Content-Type: application/json

{
  "username": "detective_jane",
  "password": "secure_password"
}

Response: 200 OK
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
  "user_id": 1,
  "email": "jane@example.com"
}
```

### Create a New Case
```
POST /cases/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
Content-Type: application/json

{
  "title": "The Missing Heirloom",
  "description": "A valuable painting disappeared from the museum on March 15th...",
  "image": "https://example.com/image.jpg",
  "is_open": true
}

Response: 201 Created
{
  "id": 1,
  "title": "The Missing Heirloom",
  "description": "...",
  "image": "https://example.com/image.jpg",
  "is_open": true,
  "date_created": "2026-02-02T10:30:00Z",
  "owner": 1
}
```

### Get User Statistics
```
GET /user/stats/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

Response: 200 OK
{
  "cases_count": 3,
  "judgments_count": 15
}
```

### Submit a Judgement
```
POST /judgements/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
Content-Type: application/json

{
  "verdict": true,
  "comment": "The evidence clearly points to guilt",
  "anonymous": false,
  "case": 1
}

Response: 201 Created
{
  "id": 1,
  "verdict": true,
  "comment": "The evidence clearly points to guilt",
  "anonymous": false,
  "case": 1,
  "supporter": 1
}
```

### Update User Profile
```
PUT /user/profile/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
Content-Type: application/json

{
  "email": "newemail@example.com",
  "password": "new_password"
}

Response: 200 OK
```

### Delete User Account
```
DELETE /user/profile/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

Response: 204 No Content
```

## Database Schema

The application uses the following models:

### CustomUser
- Extends Django's AbstractUser
- Fields: username, email, password, first_name, last_name, etc.

### Case
- `title` (string, max 200 chars)
- `description` (text)
- `image` (URL)
- `is_open` (boolean)
- `date_created` (datetime, auto)
- `owner` (ForeignKey to CustomUser)

### Judgement
- `verdict` (boolean - guilty/not guilty)
- `comment` (string, max 200 chars)
- `anonymous` (boolean)
- `case` (ForeignKey to Case)
- `supporter` (ForeignKey to CustomUser)

## Project Structure

```
crowdfunding_backend/
├── crowdfunding/                 # Main project directory
│   ├── manage.py
│   ├── db.sqlite3
│   ├── cases/                    # Cases app
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── permissions.py
│   │   ├── urls.py
│   │   └── migrations/
│   ├── users/                    # Users app
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── migrations/
│   └── crowdfunding/             # Settings
│       ├── settings.py
│       ├── urls.py
│       ├── asgi.py
│       └── wsgi.py
├── requirements.txt
├── Procfile                      # Heroku deployment config
└── README.md
```

## Future Enhancements

- [ ] Implement one-judgement-per-case limit per user
- [ ] Add gamification system (levels, badges, achievement streaks)
- [ ] Leaderboard ranking by judgement accuracy
- [ ] Advanced case filtering and search
- [ ] Discussion/comment threads for cases
- [ ] Real verdict integration and outcome tracking
- [ ] Email notifications
- [ ] User reputation system
- [ ] Case recommendation engine
- [ ] Mobile app support

## Deployment

The application is configured for deployment on Heroku using the provided `Procfile`:

```bash
git push heroku main
heroku run python crowdfunding/manage.py migrate
heroku run python crowdfunding/manage.py createsuperuser
```

## Contributing

Please follow these guidelines when contributing:
1. Create a new branch for each feature
2. Write clear, descriptive commit messages
3. Test your changes thoroughly
4. Submit a pull request with a detailed description

## Licence

This project is open source and available under the MIT Licence.

## Support

For issues, questions, or suggestions, please create an issue in the repository.

## Planning:
### Concept/Name
A crowd-powered platform where the public helps "try" cases and mysteries in the court of public opinion. Users can review details of real cases and vote on who they believe is guilty.

### Intended Audience/User Stories
Users - Victims who feel the justice system has failed them or can't access it, or for crimes that are petty and would not be put before a jury. 
Audience - True crime enthusiast, civil-minded citizens, gamified social media users, social justice warriors, investigators and nosy people. 

### Front End Pages/Functionality
=> Log in
 - Log in
  - Sign up
  
=> Homepage
  - Featured cases (spotlighted by popularity, urgency, or recency).
  - Search bar + filters (by case type: murder, fraud, cold case, celebrity scandal, etc.).

=> Case Detail Page
  - Case summary: timeline, suspects, evidence (text, images).
  - Voting options: "Guilty" / "Not Guilty" 
  - Voting stats displayed in real time (pie chart or percentages).
  - Comment/discussion section for arguments & theories.
  - "Related cases" sidebar to keep users engaged.

=> Voting / Verdict Submission Page
  - Clean UI for making a vote quickly.
  - Confirmation + optional reasoning (short text or multiple-choice).
  - Social share option: "I just voted on Case X."

=> Leaderboards & Stats
  - Top users by accuracy (how often their vote aligned with majority or real verdicts).
  - "Detective Rank" gamification system (levels, badges, streaks).



### API Spec
| URL             | HTTP Method               | Purpose | Request Body                  | Success Response Code | Authentication/Authorisation |
| --------------- | ------------------------- | ------- | ----------------------------- | --------------------- | ---------------------------- |
| /users/ | POST | Create a new user | JSON  | 201 | Any new user |
| /api-token-auth/ | POST | Get auth token    | JSON  | 200  | Authorised user |
| /cases/ | POST | Create new case | JSON Payload | 201 | Any logged in user |
| /cases/1/ | PUT | Update cases | JSON  | 200 | Authorised logged in user who created the case only |
| /cases/1/  |  GET | Retrieve a single case | N/A | 200 | Any user |
| /cases/ | GET | Retrieve all cases | N/A | 200 | Any user|
| /judgements/ | POST | Create new judgement/verdict | JSON | 201 | Authorised user only |
| /judgements/ | GET | Retrieve all judgements/verdicts | JSON | 200 | Any user |
| /judgements/1/ | PUT | Update a verdict/judgement | JSON | 200 | Authorised user only |

Short step-by-step:
=> Register a new user
  - Endpoint / Method: POST /users/
  - Request body (required): username, password
  - Auth: none
  - Success: 201 Created

=> Authenticate (get token)
  - Endpoint / Method: POST /api-token-auth/
  - Request body (required): username, password
  - Auth: none
  - Success: 200 OK — response returns an auth token to use for protected endpoints

=>Create a new case
  - Endpoint / Method: POST /cases/
  - Auth: required (logged-in user token, use the above token request in the "auth" selection, )
  - Request body (minimum): title (string, max 200 char), description (string), image (url) and is_open (boolean)
  - Success: 201 Created (returns created case with id, owner and date_created)


### DB Schema
![DB_Schema](image-1.png)
![GET_all_cases](GET_all_cases.png)
![POST_](POST_new_judgement.png)
![POST_token_return](POST_token_return.png)


!!!!Future developments, only let people judge once
### Concept/Name
A crowd-powered platform where the public helps “try” cases and mysteries in the court of public opinion. Users can review details of real cases and vote on who they believe is guilty.

### Intended Audience/User Stories
Users - Victims who feel the justice system has failed them or can't access it, or for crimes that are petty and would not be put before a jury. 
Audience - True crime enthusiast, civil-minded citizens, gamified social media users, social justice warriors, investigators and nosy people. 

### Front End Pages/Functionality
=> Log in
 - Log in
  - Sign up
  
=> Homepage
  - Featured cases (spotlighted by popularity, urgency, or recency).
  - Search bar + filters (by case type: murder, fraud, cold case, celebrity scandal, etc.).

=> Case Detail Page
  - Case summary: timeline, suspects, evidence (text, images).
  - Voting options: “Guilty” / “Not Guilty” 
  - Voting stats displayed in real time (pie chart or percentages).
  - Comment/discussion section for arguments & theories.
  - “Related cases” sidebar to keep users engaged.

=> Voting / Verdict Submission Page
  - Clean UI for making a vote quickly.
  - Confirmation + optional reasoning (short text or multiple-choice).
  - Social share option: “I just voted on Case X.”

=> Leaderboards & Stats
  - Top users by accuracy (how often their vote aligned with majority or real verdicts).
  - “Detective Rank” gamification system (levels, badges, streaks).



### API Spec
| URL             | HTTP Method               | Purpose | Request Body                  | Success Response Code | Authentication/Authorisation |
| --------------- | ------------------------- | ------- | ----------------------------- | --------------------- | ---------------------------- |
| /users/ | POST | Create a new user | JSON  | 201 | Any new user |
| /api-token-auth/ | POST | Get auth token    | JSON  | 200  | Authorised user |
| /cases/ | POST | Create new case | JSON Payload | 201 | Any logged in user |
| /cases/1/ | PUT | Update cases | JSON  | 200 | Authorised logged in user who created the case only |
| /cases/1/  |  GET | Retrieve a single case | N/A | 200 | Any user |
| /cases/ | GET | Retrieve all cases | N/A | 200 | Any user|
| /judgements/ | POST | Create new judgement/verdict | JSON | 201 | Authorised user only |
| /judgements/ | GET | Retrieve all judgements/verdicts | JSON | 200 | Any user |
| /judgements/1/ | PUT | Update a verdict/judgement | JSON | 200 | Authorised user only |

Short step-by-step:
=> Register a new user
  - Endpoint / Method: POST /users/
  - Request body (required): username, password
  - Auth: none
  - Success: 201 Created

=> Authenticate (get token)
  - Endpoint / Method: POST /api-token-auth/
  - Request body (required): username, password
  - Auth: none
  - Success: 200 OK — response returns an auth token to use for protected endpoints

=>Create a new case
  - Endpoint / Method: POST /cases/
  - Auth: required (logged-in user token, use the above token request in the "auth" selection, )
  - Request body (minimum): title (string, max 200 char), description (string), image (url) and is_open (boolean)
  - Success: 201 Created (returns created case with id, owner and date_created)


### DB Schema
![DB_Schema](image-1.png)
![GET_all_cases](GET_all_cases.png)
![POST_](POST_new_judgement.png)
![POST_token_return](POST_token_return.png)


!!!!Future developments, only let people judge once