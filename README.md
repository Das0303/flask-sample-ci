## Flask Sample CI/CD Pipeline

A minimal Flask web application demonstrating a full Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions.

This project implements a standard Git feature-branch workflow (feature/branch $\rightarrow$ dev $\rightarrow$ main) where all code changes are validated via automated tests before being merged to the primary branches.

_______________________________________________________________________________________________________________________

⚙️ Key Technologies:

-  Application Framework: Flask (Python)
-  Testing: Pytest (Python unit testing)CI/CD 
-  Tool: GitHub Actions
-  Workflow: Feature-branch Git Flow (main $\leftrightarrow$ dev $\leftrightarrow$ feature/branch)

_______________________________________________________________________________________________________________________

🚀 CI/CD Pipeline Overview :

The pipeline is defined in .github/workflows/test.yml and is triggered on all Pull Requests targeting the dev or main branches.

Pipeline Stages : 

- Trigger: A Pull Request is opened against the dev or main branch.
- Checkout: The code is checked out from the repository.
- Setup Environment: A Python environment (3.x) is set up.
- Install Dependencies: Flask and pytest are installed via requirements.txt.
- Run Tests: The pytest suite is executed.
- Status Check: Only if all tests pass will the Pull Request be allowed to merge, promoting stability.

_____________________________________________________________________________________________________________________

📂 Project Structure :

<img width="422" height="134" alt="image" src="https://github.com/user-attachments/assets/3bbcfc25-5729-481f-a089-ed47bec33754" />

______________________________________________________________________________________________________________________



