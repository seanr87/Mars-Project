# Mars-Project

This repository is all about planning and organizing a **Surviving Mars** campaign using GitHub’s workflow tools—Issues, Projects (for Gantt timelines), and a Wiki.

## Purpose

- **Centralize Our Surviving Mars Strategy**: Track every phase of colony development, from the first rocket landing to terraforming.
- **Automate Issue Creation**: Use a CSV import to quickly spin up tasks.  
- **Visualize Progress**: Leverage GitHub Projects to see milestones and tasks on a timeline.

## Key Elements

1. **CSV File (`issues.csv`)**  
   - Contains all our planned issues (milestone tasks) with titles, bodies, and labels.  
   - Used alongside the `import_issues.py` script to bulk-create GitHub Issues.

2. **`import_issues.py` Script**  
   - Reads tasks from `issues.csv` and creates corresponding Issues in our GitHub repo.  
   - Perfect for quickly setting up or updating tasks en masse.

3. **Wiki**  
   - Serves as our documentation hub.  
   - Includes pages for **Milestones**, the **Import Issues Script Overview**, and more.  
   - Also provides extra context on our Surviving Mars strategy and timelines.

4. **GitHub Projects**  
   - We have two roadmap views:
     - [**Milestones Roadmap**](https://github.com/users/seanr87/projects/4/views/1) (shows overall progress)  
     - [**Individual Tasks Roadmap**](https://github.com/users/seanr87/projects/4/views/2) (detailed tasks)  
   - These Gantt-style timelines help us monitor start dates and target dates for each milestone or sub-task.

## How to Get Started

1. **Clone the Repository**  
   - `git clone https://github.com/seanr87/Mars-Project.git`  
   - Or simply download the ZIP.

2. **Import the Issues (Optional)**  
   - Make sure you have Python installed.  
   - Update `import_issues.py` with your GitHub token and repo info (if needed).  
   - Modify or replace the default `issues.csv` if you want custom tasks.  
   - Run the script:  
     ```bash
     python import_issues.py
     ```

3. **Check the Wiki**  
   - Head over to the Wiki to see our **Milestones** breakdown, timeline disclaimers, and additional strategy notes.

4. **Explore the Roadmaps**  
   - Use the linked Project views to see high-level or detailed Gantt charts of our tasks and milestones.

## Roadmap & Future Updates

- We may refine our current Start/Target Dates as the colony evolves and our priorities change.  
- Feel free to adapt or fork the repo for your own Surviving Mars campaign.

---

Happy colonizing on Mars!
