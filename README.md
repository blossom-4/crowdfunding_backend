# Crowdfunding Back End
Break the Ceiling

## Planning:
### Concept/Name
Warning: falling glass, women rising, patriarchy under demolition. Break the ceiling not the bank. 

### Intended Audience/User Stories
Activist, advocates and allies.

### Front End Pages/Functionality
- Homepage
  - Featured fundraiser
- Search page
  - Search specific fundraiser
-   
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}
  - 

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL             | HTTP Method               | Purpose | Request Body                  | Success Response Code | Authentication/Authorisation |
| --------------- | ------------------------- | ------- | ----------------------------- | --------------------- | ---------------------------- |
| /fundraisers    | Fetch all the fundraisers | GET     | N/A                           | 200                   | None                         |
| /fundraisers    | Create new fundraiser     | POST    | JSON Payload                  | 201                   | Any logged in user           |
| /fundraisers/1/ |                           |         |                               |                       |                              |
| /fundraisers    |                           | GET     | N/A                           | 200                   |                              |
| /fundraisers    | Create new pledge         | POST    | {"fundraiser_id} JSON Payload | 201                   | Any logged in user           |
### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )