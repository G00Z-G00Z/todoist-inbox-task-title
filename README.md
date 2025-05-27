# ToDoist Inbox Task Title

Small script that retrieves the tasks titles for todoist and copies it to your clipboard. This can be used later to integrate with another app

## Setup

The only setup you need is to fill up the environment with `TODOIST_API_TOKEN` which is the token for integration you getfrom the app. You can either have it in your environment or as a `.env` file

Run:

```bash
./todoist_inbox_retrieve.py
```

To get the titles copied to your clipboard

## Development

It uses `uv` as a python packet manager
