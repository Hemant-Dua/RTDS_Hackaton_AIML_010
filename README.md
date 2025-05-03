├── app/
│   ├── __init__.py                  # Initializes the backend app
│   ├── main.py                      # Entry point for the app (API server setup)
│   ├── config.py                    # Configuration file (API keys, DB settings)
│   ├── api/
│   │   ├── __init__.py              # API module initializer
│   │   ├── routes.py                # API endpoint routing
│   │   ├── request_handler.py       # Handles user queries
│   │   ├── openstack_api.py         # Functions for interacting with OpenStack APIs
│   │   ├── ai_classifier.py         # Functions for intent classification
│   │   ├── parameter_extractor.py   # Extract parameters from user query
│   │   └── confirmation_handler.py  # Ask for confirmation for destructive actions
│   ├── services/
│   │   ├── __init__.py              # Service module initializer
│   │   ├── session_manager.py       # Manage user sessions for multi-step actions
│   │   ├── database.py              # DB interactions (logging user queries and actions)
│   │   └── logger.py                # Logging service for tracking actions and errors
│   ├── utils/
│   │   ├── __init__.py              # Utility functions
│   │   └── utils.py                 # Miscellaneous helper functions
│   └── templates/                   # HTML, CSS, JS (for frontend, if used)
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Dockerfile for containerization
├── docker-compose.yml               # Docker compose file (if using multiple services)
└── README.md                        # Project documentation
