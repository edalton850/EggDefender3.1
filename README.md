# Egg Defender (v3.1)

**IBM Applied Software Engineering Capstone Project**

A modular, turn-based tactical puzzle game built with **Python** and **Pygame CE**. This project demonstrates professional SDLC practices, architectural modularity, and "Process Intensity 0.3" workflows.

---

## Project Vision

**Egg Defender** is a tactical puzzle game built on the "Ava Moreno Canon" design framework. It challenges the traditional "Tower Defense" trope by enforcing a **"No Punishment, Only Puzzles"** philosophy. The player protects a fragile objective (The Egg) using positioning, patience, and logic rather than brute force.

### Key Features

* **Hexagonal Grid System:** Custom axial coordinate system (q, r) with flat-top hex rendering.
* **Modular Architecture:** Strict separation of concerns between GridSystem, EntitySystem, and GameManager.
* **WebAssembly Ready:** Designed for browser deployment via pygbag (targeting 60FPS on low-end devices).
* **Turn-Based Logic:** Deterministic state machine managing Player vs. Environment turns.

## Technical Architecture

This project adheres to **Object-Oriented Programming (OOP)** principles and **Modular Design**.

| Module | Responsibility |
| --- | --- |
| **main.py** | Bootstrap, Game Loop, and Event Handling (Asyncio). |
| **grid_system.py** | Hexagon mathematics, coordinate conversion (Axial-Pixel), and grid rendering. |
| **entity_system.py** | Entity state management, polymorphism (Hero/Egg classes), and movement validation. |

### Tech Stack

* **Language:** Python 3.13.19
* **Engine:** Pygame CE (Community Edition) 2.5.6
* **Build Tool:** pygbag (WASM/HTML5 Export)
* **Methodology:** Agile/Iterative (Sprint-based SDLC)

## Installation & Usage

### Prerequisites

* Python 3.10+
* pip

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/edalton850/EggDefender3.1.git
cd EggDefender3.1

```


2. **Install dependencies:**
```bash
pip install pygame-ce

```


3. **Run the game:**
```bash
python main.py

```



## Project Structure

```text
EggDefender3.1/
├── main.py              # Application entry point
├── grid_system.py       # Hex grid logic & rendering
├── entity_system.py     # Player & Enemy logic
├── assets/              # Game assets (sprites, sfx)
├── docs/                # Architecture & Design documentation
└── README.md            # Project documentation

```

---

*Created by [Erin Dalton](https://www.google.com/search?q=https://www.linkedin.com/in/erinjdalton/) - IBM Software Engineering Specialization*
