# Automated-Weather-Sender <img src="https://cdn-icons-png.flaticon.com/512/2134/2134677.png" width="50"> 

This repository automatically sends the weather of the current day to a certain email address on Sunday through Thursday at 20:00 PM using deta cloud platform. (FREE)

## Requirements

Install the dependencies with pip

```
requests
python-dotenv
```

[FOR WINDOWS] Install the Deta CLI, open PowerShell and enter:

```iwr https://get.deta.dev/cli.ps1 -useb | iex```

[FOR MAC] Install the Deta CLI, open terminal and enter:

```curl -fsSL https://get.deta.dev/cli.sh | sh```

## Deployment
**Official Documentation:** https://docs.deta.sh/docs/micros/getting_started <br/>

[FOR WINDOWS and MAC] 
To deploy this project you:
1) login via the deta CLI
```
  deta login
```
2) create a new micro (only once!)
```
  deta new --python first_micro
```
3) upload your environment variables
```
  deta update -e <env_file_name>
```
4) deploy your app
```
  deta deploy
```
5) set the cron job 
  Examples:

  Run every minute

```
  deta cron set "1 minute"
```
  Run from Monday until Friday at 18:00 PM (UTC)

```
  deta cron set "0 18 ? * MON-FRI *"
```
## And you DONE! 

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file <br/>
`EMAIL`
`PASSWORD`
`API_KEY`
`PASSWORD`
RECEIVER_EMAIL
