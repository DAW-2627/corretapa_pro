# 🍢 Tapas Bar Reservation System — Modularization & Git Workflow Exercise

> **Note to Visitors:** This repository contains an educational programming exercise designed for software development students. The initial codebase is intentionally structured as a single, monolithic Python script. The goal of this project is for students to practice **code refactoring**, **modular architecture**, **pair programming**, and **collaborative Git/GitHub workflows** (branching, pull requests, and parallel development).

---

## 🎯 Project Overview

The application is a command-line interface (CLI) tool written in Python that manages table reservations and promotional discounts for local tapas bars. Currently, all data, business logic, configuration, and user interface code live in a single unmanageable file.

## 🚀 Your Mission (Pair Programming)

Working in pairs, your objective is to refactor this monolithic script into a **clean, modular architecture consisting of 5 specialized files**. To simulate a real-world parallel development environment, you will divide the responsibilities using Git branches and merge your work together.

### 👨‍💻 Role A: Data & Business Logic Architect
*Responsible for state, data structures, and pure computational logic.*

* **`config.py`**: Define global constants, settings, and business rules.
* **`dades_bars.py`**: Manage bar collections, table availability, and data queries.
* **`logica_promo.py`**: Implement pure discount and promotion algorithms *(strictly no `input()` or `print()` statements allowed in this module)*.

### 👩‍💻 Role B: Interface & Control Flow Architect
*Responsible for user interaction, input validation, and application orchestration.*

* **`interficie.py`**: Build CLI menus, display outputs, and handle user input with proper error/exception handling.
* **`main.py`**: Act as the clean entry point and orchestrator that connects Role A's modules with Role B's interface.
* **Integration Testing**: Execute the final end-to-end test suite to verify that all interconnected modules work seamlessly together.

---

## 🛠️ Recommended Git Workflow

1. **Fork / Clone** this repository to your local machines.
2. Create separate **feature branches** for each role (e.g., `feature/data-logic` for Role A and `feature/ui-flow` for Role B).
3. Agree on **function signatures and data contracts** before coding so both modules integrate smoothly.
4. Commit frequently with clear, descriptive messages.
5. Open **Pull Requests (PRs)** to merge your branches into `main`, resolving any merge conflicts together.

---

## 📋 Requirements

* Python 3.8+
* Standard library only (no external dependencies required)

