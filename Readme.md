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
├── scripts/           # Python scripts
├── visualizations/    # Generated plots and charts
└── README.md         # Project documentation
```

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

*No datasets or advanced computations are required.*

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
