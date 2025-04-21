# What's Up Dawg?!

A simulation game that lets you experience life as a dog and its human companion. Perfect for prospective dog owners looking to understand the responsibilities and joys of pet ownership.

## 🎮 Overview

What's Up Dawg?! is an educational simulation game developed as part of the University of Oregon's CS422/522 Software Methodologies Project 2. The game provides players with an immersive experience of managing a dog's life, including care, training, and daily activities.

## 👥 Project Contributors

- Anna Finlay
- Morgan Jones
- Ethan Reinhart
- Darby Wright

**Development Period:** February 15, 2024 - March 11, 2024  
**Course:** University of Oregon - CS422/522 Software Methodologies Project 2, Group 7

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or above

### First-Time Setup
1. Open a terminal window
2. Navigate to the root folder
3. Run the following command:
   ```bash
   sh CLICKME.sh
   ```
   This will install all required dependencies and launch the application.

### Subsequent Runs
You can either:
- Use the same command as above (`sh CLICKME.sh`)
- Or run directly with Python:
  ```bash
  python3 ./src/app.py
  ```

## 📁 Project Structure

```
.
├── docs/               # Documentation and resources
│   ├── dog_info/      # Dog-related information and research
│   ├── images/        # Project images
│   └── meetings/      # Development process meeting notes
│
├── src/               # Source code
│   ├── data/         # Static data and resources
│   │   ├── shop_items.py
│   │   ├── afflictions.py
│   │   ├── events.py
│   │   ├── dog_breeds.py
│   │   └── scraper.py
│   │
│   ├── app.py        # Main application file
│   ├── controller.py # Game controller
│   └── model.py      # Game model
│
└── CLICKME.sh        # Setup and launch script
```

## 💻 Technical Details

- The game is built using Python 3.10+
- All code is original and created by the project team
- The only exception is the ToolTip implementation in `./src/app.py`, which is properly attributed with source information

## 📝 License

This project is part of a university course assignment. All rights reserved.

## 🤝 Contributing

This is a course project and is not open for contributions. However, we welcome feedback and suggestions for improvement.

---

*For more information about the game mechanics and features, please refer to the documentation in the `docs/` directory.* 