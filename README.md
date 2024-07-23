# GPU Runtime Password Cost Calculator

## Overview
This project estimates the cost in GPU runtime to crack a password, providing a more economically relevant metric than traditional password strength meters.

## Features
- **Cost Estimation:** Approximate GPU runtime cost to crack a password.
- **Adjustable Parameters:** Customize time frame, GPU type, and electricity cost.
- **Real-Time Data:** Up-to-date pricing and performance data for various GPUs.
- **Secure Design:** Client-side password calculations to maintain privacy.

## How It Works
1. **Input:** Enter password and set constraints (e.g., time frame, GPU model).
2. **Calculation:** Estimate attempts and calculate cost based on GPU pricing.
3. **Output:** Detailed report on the estimated cost.

## How to Run
1. **Clone the repository:**
    ```bash
    git clone https://github.com/ivantko/gpu-runtime-password-cost-calculator.git
    cd gpu-runtime-password-cost-calculator
    ```
2. **Set up the virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the application:**
    ```bash
    python main.py
    ```

## Project Status
- **Basic Structure:** Initial setup and routing.
- **Initial Logic:** Basic cost calculation logic.
- **Testing:** Initial functionality tests.

## Target Audience
- **Security Enthusiasts**
- **Educators**
- **Researchers**

## Collaboration Welcome
**Join the Effort:** Contributions are welcome. Fork the repo, create a feature branch, develop and test your changes, and submit a pull request.

## Get in Touch
Questions or ideas? Contact me via:
- Email: [iv.tko@pm.me](mailto:iv.tko@pm.me)
- GitHub: [@ivantko](https://github.com/ivantko)

Let's collaborate to make this tool both powerful and user-friendly!

```mermaid
graph LR
    A[User Input] --> B[Estimate Attempts]
    B --> C[Calculate Cost]
    C --> D[Output Report]
    D --> E[User]
```