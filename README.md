## Vaccine Slot Finder

### Find the Vaccine Slot

The vaccine slot finder can be used to find the slot on the basis of age, pincode, district or location and notify you via email, slack or google chat.

### Usage

- Clone the code
- Install the dependencies `pip install -r requirements.txt`
- Copy the .env.example file as .env and update the value according to the usage

| Variable Name        | Value                                         | Details                                                           |
| -------------------- | --------------------------------------------- | ----------------------------------------------------------------- |
| PINCODE              | 175011                                        | comma separated pincode if you want to fetch more than 1 pin code |
| START_DATE           | 02-05-2021                                    | Start Date                                                        |
| NOTIFICATION_CHANNEL | SLACK,gchat,email                             | Notification Channel you want to get notification                 |
| EMAIL                | send@email.com                                | email will be sent on this email                                  |
| SMTP_SERVER          | smtp.gmail.com                                | SMTP server e.g smtp.gmail.com                                    |
| SMTP_PORT            | 587                                           | SMTP PORt                                                         |
| SENDER_PASSWORD      | password/app-password                         | Password for SMTP                                                 |
| SENDER_EMAIL         | smtp_email                                    | Email of sender                                                   |
| SUBJECT              | Notification Regarding the Covid Vaccine Slot | Custom Subject                                                    |
| MIN_AGE              | 15                                            | Minimum Age                                                       |
| MAX_AGE              | 60                                            | Maximum Age                                                       |
| MIN_REQUIRED         | 3                                             | Minimum no of slots required                                      |
| SLACK_WEBHOOK        | Slack webhook url                             | Notification for slack URL                                        |
| GCHAT_WEBHOOK        | Gchat room webhook                            | Notification for Gchat URL                                        |
| DISTRICTS            | 187,129                                       | List of comma separated districts                                 |

- Run the code via `python vaccine.py`

### Use as Docker

- Build the docker image using `docker build -t <image_name> .`
- Run the code `docker run <image_name>`

The above code can be used as trigger from AWS lambda

**For fetching the details of the district id, please check `districts_list.csv`**
