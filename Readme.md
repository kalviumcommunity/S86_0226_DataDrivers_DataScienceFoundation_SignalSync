📊 SIGNAL SYNC
Urban Traffic Congestion Analysis (Real-World Data Project)

Team Name: Data Drivers

1. Introduction

Urban areas are experiencing increasing traffic congestion due to rapid population growth and the continuous rise in vehicle usage. Although large volumes of traffic sensor data are collected daily, much of this data remains underutilized for practical traffic management and planning decisions.

Signal Sync is a data-driven project that analyzes real-world highway traffic volume data to uncover meaningful patterns and insights. The project aims to support smarter traffic management strategies and contribute to improved urban infrastructure planning through systematic data analysis.

2. Problem Statement

Urban planners collect extensive traffic sensor data but often lack actionable insights to effectively manage congestion.

This project focuses on analyzing highway traffic data to identify:

Congestion hotspots

Peak travel hours

Recurring traffic bottlenecks

Weekly and seasonal congestion trends

The ultimate objective is to enable data-driven infrastructure planning and improve traffic signal optimization strategies.

3. Dataset Description

Source: Kaggle
Dataset Name: galenchen/highway-traffic-volume

Dataset Features

date_time – Timestamp of traffic observation

traffic_volume – Number of vehicles observed

installing-python-and-anaconda-on-the-local-machine

Weather-related features (temperature, rain, snow, etc.)

This dataset supports time-based analysis and pattern recognition for traffic congestion studies.
main

4. Tech Stack

installing-python-and-anaconda-on-the-local-machine

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

The project was developed using the following technologies:

Python

NumPy

Pandas
main

Matplotlib

Seaborn

Jupyter Notebook

These tools were used for data cleaning, feature engineering, visualization, and exploratory data analysis (EDA).

## 5. Project Setup Instructions

### Prerequisites

Before setting up the project, ensure you have:

- **Python 3.8+** installed on your system
- **Anaconda** or **Miniconda** for environment management
- **Git** for version control

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kalviumcommunity/S86_0226_DataDrivers_DataScienceFoundation_SignalSync.git
   cd S86_0226_DataDrivers_DataScienceFoundation_SignalSync
   ```

2. **Create Conda Environment**

   ```bash
   conda create -n signalsync python=3.9
   conda activate signalsync
   ```

3. **Install Required Packages**

   ```bash
   pip install pandas numpy matplotlib seaborn jupyter kagglehub
   ```

   Or install from requirements (if available):

   ```bash
   pip install -r requirements.txt
   ```

### Environment Verification

4. **Verify Installation**

   ```bash
   python -c "import pandas, numpy, matplotlib, seaborn; print('✅ All packages installed successfully')"
   ```

5. **Launch Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

   - Navigate to the notebooks folder in the Jupyter interface
   - Open the project notebooks to begin analysis

### Dataset Setup

6. **Download Dataset** (When ready for analysis)
   ```python
   import kagglehub
   path = kagglehub.dataset_download("galenchen/highway-traffic-volume")
   print("Dataset downloaded to:", path)
   ```

### Project Structure

```
SignalSync/
├── notebooks/          # Jupyter notebooks for analysis
├── data/              # Dataset storage
├── raw/
│ └── processed/
├── scripts/           # Python scripts
├── visualizations/    # Generated plots and charts
└── README.md         # Project documentation
```

---

## Folder Description

### `data/`

Stores all datasets used in the project.

- `raw/`  
  Contains original, unmodified datasets. These files should never be edited directly.

- `processed/`  
  Contains cleaned or transformed datasets generated from raw data.

This separation prevents accidental corruption of original data.

---

### `notebooks/`

Contains Jupyter Notebook files (`.ipynb`) used for:

- Data exploration
- Analysis
- Visualization
- Documentation using Markdown

Keeps analysis separate from reusable scripts.

---

### `scripts/`

Contains Python scripts (`.py`) for:

- Data preprocessing
- Utility functions
- Reusable logic

Helps maintain clean and modular code.

---

### `outputs/`

Stores generated results such as:

- Charts and plots
- Reports
- Exported CSV files
- Model outputs

Keeps results separate from raw and processed data.

---

### `README.md`

Provides documentation for the project including:

- Project purpose
- Folder structure explanation
- Setup instructions
- Collaboration guidelines

## 🗂️ Data Organization (Raw, Processed, and Outputs)

This project follows a clear separation of data across its lifecycle to ensure data integrity, reproducibility, and maintainability.

### 📁 Raw Data (`data/raw/`)

- Contains the original datasets exactly as received
- These files are treated as **read-only**
- Raw data is never modified or cleaned directly
- Serves as the single source of truth for the project

This preserves data integrity and allows results to be reproduced at any time.

---

### 📁 Processed Data (`data/processed/`)

- Contains cleaned and transformed datasets derived from raw data
- Files are generated programmatically from the raw data
- Uses clear and descriptive filenames to indicate processing stage
- Can always be recreated from the raw data

This ensures traceability between raw inputs and processed outputs.

---

### 📁 Output Artifacts (`outputs/`)

- Stores final and intermediate results such as:
  - Plots and visualizations
  - Tables and reports
  - Exported CSV files
  - Model outputs (if any)
- Outputs are never mixed with raw or processed data
- Uses descriptive names for easy identification

This keeps results easy to locate and review.

---

### 🔄 Data Flow Discipline

The project enforces a one-directional data flow:

**Raw Data → Processed Data → Outputs**

- Scripts read only from `data/raw/`
- Processed files are saved in `data/processed/`
- Results are saved in `outputs/`
- Raw data is never overwritten

This prevents data contamination and ensures reproducibility.

7. Project Workflow
   7.1 Data Collection

The dataset was obtained using the KaggleHub API.

7.2 Data Cleaning

Converted timestamps to datetime format

Checked and handled missing values

Extracted time-based features

7.3 Feature Engineering

installing-python-and-anaconda-on-the-local-machine

- Hour of the day
- Day of the week
- Month and year
- Congestion flag (75th percentile threshold)

The following features were created:

Hour of the day

Day of the week

Month and year
main

Congestion flag (based on the 75th percentile traffic volume threshold)

7.4 Exploratory Data Analysis (EDA)

installing-python-and-anaconda-on-the-local-machine

- Peak hour analysis
- Monthly traffic trend analysis
- Weekly traffic pattern detection
- Bottleneck detection (Day + Hour level)
- Correlation analysis

The following analyses were conducted:

Peak hour analysis

Monthly traffic trend analysis
main

Weekly traffic pattern detection

Bottleneck detection (Day + Hour level)

Correlation analysis

8. Key Insights
   Peak Hours

Rush hours consistently show higher congestion levels.

Monthly Trends

Certain months demonstrate higher traffic volumes, indicating seasonal congestion patterns.

Recurring Bottlenecks

Specific combinations of day and hour repeatedly show congestion spikes.

Launching-Jupyter-Notebook 9. Recommendations

7. Recommendations
   installing-python-and-anaconda-on-the-local-machine

- Optimize traffic signal timings during peak hours
- Deploy traffic personnel during high-congestion periods
- Improve infrastructure in high-volume corridors
- Encourage public transportation during heavy traffic seasons
  main

Based on the findings, the following recommendations are proposed:

Optimize traffic signal timings during peak hours
main

Deploy traffic personnel during high-congestion periods

Improve infrastructure in high-volume corridors

Encourage public transportation during heavy traffic seasons

10. Learning Outcomes

installing-python-and-anaconda-on-the-local-machine

- Experience working with real-world datasets
- Strong understanding of EDA
- Congestion detection logic development
- Actionable insight generation

Through this project, the team gained:

Practical experience working with real-world datasets

Strong understanding of Exploratory Data Analysis (EDA)

Experience in congestion detection logic development
main

Ability to generate actionable insights for urban planning

11. Conclusion

installing-python-and-anaconda-on-the-local-machine
Signal Sync demonstrates how raw traffic data can be transformed into actionable insights for smarter traffic management and infrastructure planning.

# 🧪 Environment Setup Documentation (Milestone 1)

This section documents the local development environment used for the Data Science sprint.

## Operating System

- Windows / macOS / Linux (update with your OS)

## Python Version

```bash
python --version
```

Signal Sync demonstrates how raw traffic data can be transformed into actionable insights through systematic analysis.

By identifying congestion patterns and recurring bottlenecks, this project supports smarter, data-driven traffic management and infrastructure planning decisions.

## 12. Documentation and Communication Milestone

### 📝 Writing Clear Documentation in Jupyter Notebooks Using Markdown

This milestone focuses on writing clear, readable documentation inside Jupyter Notebooks using Markdown. While code performs the analysis, Markdown explains the intent, logic, and results—making notebooks understandable to others and to your future self.

Well-written Markdown transforms notebooks from messy scratchpads into professional, review-ready artifacts that clearly communicate your thinking throughout the Data Science sprint.

#### Learning Objectives

This lesson helps you:

- Understand what Markdown cells are and how they differ from code cells
- Write headings to structure notebooks logically
- Create ordered and unordered lists for clarity
- Add inline code and code blocks for explanation
- Combine text and code to tell a clear data story

#### Milestone Outcomes

By completing this milestone, you will be able to:

- Structure notebooks using meaningful headings
- Document steps and assumptions using Markdown text
- Use lists to explain workflows and results
- Format code snippets inside Markdown cells
- Create notebooks that are readable and review-friendly

#### Why This Matters

Common notebook issues include:

- Notebooks that are hard to follow or review
- No explanation of what the code is doing
- Results shown without context or interpretation
- Confusing execution flow with no structure

These issues are not technical failures—they are **communication failures**.

This milestone ensures that:

- Your reasoning is clearly documented
- Reviewers can understand your approach
- Teammates can follow and reuse your work
- Your notebooks look professional and intentional

Think of Markdown as the narration of your analysis—this lesson teaches you how to write that narration clearly.

#### What You Are Expected to Do

This is a documentation and communication milestone, not a data analysis task.

You are expected to:

- Create Markdown cells alongside code cells
- Practice formatting text using Markdown syntax
- Focus on clarity and structure, not complex analysis
- Use simple examples to demonstrate formatting

_No datasets or advanced computations are required._

#### Key Components

##### 1. Writing Headings in Markdown

Use headings to organize notebook sections.

You should:

- Create top-level headings for major sections
- Use subheadings to break content into steps
- Maintain a logical, readable hierarchy
- Avoid overly long or vague headings

This helps readers understand the notebook flow instantly.

##### 2. Creating Lists for Structured Explanations

Use lists to explain steps, assumptions, or results.

You should:

- Write unordered lists for general points
- Write ordered lists for step-by-step processes
- Keep list items concise and meaningful
- Use lists where structure improves readability

Lists make explanations easier to scan and understand.

##### 3. Writing Inline Code and Code Blocks

Use code formatting inside Markdown to explain syntax.

You should:

- Use `inline code` for variable names or functions
- Use fenced code blocks for longer snippets
- Ensure code blocks are readable and relevant
- Avoid duplicating executable code unnecessarily

This allows you to explain code without executing it.

##### 4. Combining Markdown and Code Cells Effectively

Learn when to use Markdown vs code.

You should:

- Use Markdown before code to explain intent
- Use Markdown after code to interpret output
- Avoid placing explanations inside code comments
- Maintain a clean alternation between text and code

This creates a smooth narrative flow in notebooks.

 Creating-First-Python-Script
---

## 13. Python Script Development Milestone

### 🐍 Creating and Running Your First Standalone Python Script

This milestone focuses on creating and running your first standalone Python script for data analysis. While notebooks are great for exploration, scripts are essential for repeatable, shareable, and automation-friendly workflows.

Learning how to move from notebooks to scripts is a key step toward writing real-world Data Science code.

#### Learning Objectives

This lesson helps you:

- Understand what a Python script is and when to use it
- Create a .py file for data analysis
- Run a Python script from the command line or editor
- Print outputs and observe results
- Build confidence executing code outside notebooks

#### Milestone Outcomes

By completing this milestone, you will be able to:

- Create a basic Python script for data-related tasks
- Run scripts reliably from the terminal or editor
- Understand script execution flow from top to bottom
- Debug simple execution issues
- Use scripts alongside notebooks effectively

#### Why This Matters

Common beginner issues include:

- Relying only on notebooks for all tasks
- Not knowing how to run code outside Jupyter
- Difficulty automating or reusing analysis
- Confusion between interactive and script-based workflows

**Scripts solve these problems.**

This milestone ensures that:

- Your work is repeatable and reusable
- You can automate simple data tasks
- Your code runs consistently end to end
- You are comfortable working outside notebooks

Think of scripts as the production version of your analysis.

#### What You Are Expected to Do

This is a scripting fundamentals milestone, not a complex data analysis task.

You are expected to:

- Create a Python script file
- Write simple data-related logic
- Run the script successfully
- Observe and explain the output

*No large datasets or advanced libraries are required.*

#### Key Components

##### 1. Creating a Python Script

Create a .py file for your analysis.

You should:
- Name the script clearly
- Place it in the appropriate project folder
- Write valid Python code inside the file
- Avoid notebook-only features

This introduces script-based development.

##### 2. Writing Simple Data Logic

Add basic logic to the script.

You should:
- Define variables and simple calculations
- Work with small sample data
- Print results to the console
- Keep logic simple and readable

The focus is execution, not complexity.

##### 3. Running the Script

Execute the script.

You should:
- Run the script from a terminal or editor
- Observe printed output
- Fix basic errors if execution fails
- Understand how Python executes scripts top to bottom

This builds confidence in running code independently.

##### 4. Understanding Script vs Notebook Execution

Learn the differences.

You should:
- Understand when to use scripts vs notebooks
- Recognize the lack of persistent state in scripts
- Appreciate scripts for automation and reuse
- Avoid treating scripts like interactive notebooks

This distinction is critical for real projects.

##### 5. Video Walkthrough (~2 Minutes)

Record a short screen-capture video demonstrating your script.

Your video must include:
- The .py file in the project
- Running the script
- Observing and explaining output
- Brief explanation of why scripts are useful

#### Submission Guidelines

- Submit your work as a Pull Request (if required)
- Submit the video link as instructed
- Video should be approximately 2 minutes
- Video must be screen-facing and clearly visible

#### Important Notes

- Keep scripts simple and focused
- Avoid unnecessary complexity
- Use print statements for visibility
- Scripts are a foundation for automation

Being able to create and run Python scripts is a core professional skill. This milestone ensures you can move beyond notebooks and execute data workflows confidently.

#### Bonus Content

This section is optional, and learners who want to explore the topics covered so far can utilize the materials provided below:

- How to Run Python Scripts
- Python Scripts vs Jupyter Notebooks
- Writing Your First Python Program

---

=======
 main
🔧 **Environment Verification (Sprint Hygiene Milestone)**

This milestone verifies that the local Data Science environment is correctly configured and ready for the sprint.

This is a verification checkpoint — not an installation task.

The goal is to confirm that:

Writing-Markdown-for-Headings-Lists

- Python is installed and callable
- Conda environments function correctly
- Jupyter Notebook/Lab launches and runs Python code
- The setup is stable and reusable throughout the sprint

The setup is stable and reusable throughout the sprint
main

## 📓 Milestone: Understanding Code Cells vs Markdown Cells

**Completed:** February 25, 2026

### What Was Accomplished

This milestone focused on mastering one of the most fundamental skills in Jupyter Notebooks: distinguishing between **Code cells** and **Markdown cells**, and using each intentionally for professional Data Science work.

### Key Deliverables

1. **Created Interactive Notebook:** `Code_vs_Markdown_Cells.ipynb`
   - Demonstrates the difference between Code and Markdown cells
   - Shows when and why to use each cell type
   - Includes practical examples relevant to the Signal Sync project

2. **Notebook Structure Includes:**
   - Code cells with executable Python statements (variables, calculations, lists)
   - Markdown cells with formatted explanations, headings, and bullet points
   - Examples of proper notebook organizatioan combining both cell types
   - Step-by-step guide on switching between cell types
   - Best practices for professional notebook writing

3. **Skills Demonstrated:**
   - Creating and executing Code cells
   - Creating and rendering Markdown cells with formatting
   - Converting cells between types using keyboard shortcuts
   - Structuring notebooks for readability and collaboration
   - Separating execution logic from narrative explanation

### Why This Matters

In professional Data Science work:

- **Code cells** show _what_ you did (the logic and computations)
- **Markdown cells** explain _why_ you did it and _what it means_ (the reasoning and insights)

This milestone ensures that all notebooks created throughout the Signal Sync project are:

- ✅ Readable and reviewable by teammates
- ✅ Well-documented with clear explanations
- ✅ Structured for professional collaboration
- ✅ Easy to debug and extend in the future

### Next Steps

Moving forward, all analysis notebooks in the Signal Sync project will follow these best practices:

- Using Markdown for section headers and explanations
- Using Code for all executable logic
- Maintaining clear separation between computation and narrative
- Building notebooks that communicate insights, not just compute them

# 📓 Milestone: Running, Restarting, and Interrupting Jupyter Kernels

## Objective

- Run notebook cells in a controlled and sequential manner
- Restart the kernel to reset notebook state
- Interrupt long-running or stuck executions safely
- Understand the difference between interrupting and restarting a kernel

---

## What Was Accomplished

- Executed notebook cells one by one to observe execution order
- Observed that variables persist in memory until the kernel is restarted
- Interrupted a deliberately long-running execution
- Restarted the kernel and confirmed that all variables and memory were cleared
- Reran all cells from the top to ensure reproducibility

---

## Key Activities

### Running Cells and Execution Order

- Ran cells sequentially
- Observed how outputs depend on execution order

### Interrupting Execution

- Safely interrupted a long-running cell
- Verified the notebook remained responsive

### Restarting the Kernel

- Restarted the kernel from the Jupyter menu
- Cleared all variables and memory
- Reran all cells from the beginning

### Restart vs Interrupt

- Identified scenarios where interrupting execution is sufficient
- Identified scenarios where restarting the kernel is safer

---

## Skills Demonstrated

- Understanding kernel states (idle, running, interrupted)
- Safe interruption of stuck executions
- Proper kernel restart and memory reset
- Clean and reproducible notebook execution
  main

---

# 📊 Milestone: Python Data Types - Numeric and String Fundamentals

## 🎯 Milestone Overview

This milestone focuses on understanding Python's core numeric and string data types, which form the foundation of all data processing and analysis. Before working with datasets, you must be comfortable representing numbers, text, and basic operations correctly.

Clear understanding of data types prevents logical errors and makes your code predictable, readable, and reliable.

---

## 🎓 Learning Objectives

This lesson is to help you:

- Understand numeric data types like integers and floats
- Understand string data and text representation
- Perform basic operations on numbers and strings
- Identify type-related issues early
- Use data types intentionally in programs

---

## 📋 Milestone Outcomes

By completing this milestone, you will be able to:

- Differentiate between numeric and string data types
- Perform arithmetic using Python numbers
- Manipulate and format strings correctly
- Identify data type mismatches
- Write clearer and safer Python code

---

## ⚠️ Why This Matters

Common beginner issues include:

- Treating numbers as strings accidentally
- Unexpected results from arithmetic operations
- Concatenation errors with text and numbers
- Confusion when printing or formatting outputs

These issues usually come from misunderstanding data types.

This milestone ensures that:

- Your calculations behave as expected
- Your text data is handled correctly
- Errors are easier to debug
- Your programs are logically sound

**Think of data types as the language Python uses to understand your data.**

---

## 📝 What You Are Expected to Do

This is a Python fundamentals milestone, not a data analysis task.

You are expected to:

- Work with numeric and string variables
- Perform simple operations using each type
- Print results to observe behavior
- Identify differences between numbers and text

**No datasets or advanced libraries are required.**

---

## 🔢 1. Working with Numeric Data Types

Learn how Python represents numbers.

You should:

- Use integers and floating-point numbers
- Perform basic arithmetic operations
- Observe how Python handles division
- Understand numeric precision at a basic level

This builds confidence in numerical computations.

---

## 📝 2. Understanding String Data Types

Learn how Python represents text.

You should:

- Create string variables
- Concatenate strings
- Access string values
- Print strings clearly

Strings are essential for labels, messages, and data fields.

---

## 🔀 3. Mixing Numbers and Strings Safely

Understand how Python treats mixed types.

You should:

- Observe errors when mixing types incorrectly
- Convert numbers to strings when needed
- Convert strings to numbers carefully
- Understand when explicit conversion is required

This prevents runtime errors.

---

## 🔍 4. Inspecting Data Types

Learn how to check variable types.

You should:

- Inspect variable types during execution
- Understand why type awareness matters
- Use type checks to debug issues
- Build habits of validating data early

Type awareness improves code correctness.

---

## 🎥 5. Video Walkthrough (~2 Minutes)

Record a short screen-capture video demonstrating numeric and string data types.

Your video must include:

- Numeric variable examples
- String variable examples
- Operations on both types
- Explanation of type differences and behavior

---

## 📤 Submission Guidelines

- Submit your work as a Pull Request (if required)
- Submit the video link as instructed
- Video should be approximately 2 minutes
- Video must be screen-facing and clearly visible

---

## 📌 Important Notes

- This milestone focuses on fundamentals
- Keep examples simple and intentional
- Avoid complex logic or edge cases
- Strong basics prevent larger bugs later

Understanding data types is a core programming skill. This milestone ensures you can work confidently with numbers and text throughout the Data Science sprint.

---

## 🎁 Bonus Content

This section is optional, and learners who want to explore the topics covered so far can utilize the materials provided below.

- [Python Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Python Strings Explained](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Type Conversion in Python](https://docs.python.org/3/library/functions.html#int)

---

**Good luck with your milestone!**
