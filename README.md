# Crowdfunding Back End
Raise the Case

## Planning:
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