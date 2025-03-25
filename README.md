# 🚀 Drone Delivery Optimization

## 📌 Project Overview
This project optimizes the assignment of delivery orders to drones while ensuring:
- Orders are delivered **within the deadline**.
- Drones **do not exceed their maximum payload**.
- The **shortest route is taken** to minimize travel time.
- **Multiple orders can be assigned** to a single drone if conditions allow.
- Drones **return to the starting point (0,0)** after completing deliveries.

---

## 📦 Features
✅ Assigns **multiple orders** to a single drone if possible.  
✅ Uses **Manhattan Distance** to calculate the shortest route.  
✅ Ensures **weight, distance, and time constraints** are met.  
✅ Returns drones to `(0,0)` after deliveries.  
✅ Outputs results in a **structured JSON format**.  

---

## 🔧 Installation
1. **Clone the repository** (or create a folder and place the script inside).  
2. **Ensure Python is installed** (`>=3.6`).  
3. **Install dependencies (if required):**
```bash
pip install pandas
```
4. **Run the script:**
```bash
python drone_delivery_optimizer.py
```

---

## 📂 Input JSON Format (`input.json`)
```json
{
    "city": { "grid_size": 30 },
    "drones": { "fleet": [
        { "id": "D1", "max_payload": 15, "max_distance": 80, "speed": 3, "available": true },
        { "id": "D2", "max_payload": 10, "max_distance": 50, "speed": 2.5, "available": true },
        { "id": "D3", "max_payload": 7, "max_distance": 30, "speed": 2, "available": true }
    ] },
    "orders": [
        { "id": "O1", "delivery_x": 4, "delivery_y": 6, "deadline": 20, "package_weight": 5 },
        { "id": "O2", "delivery_x": 7, "delivery_y": 3, "deadline": 25, "package_weight": 6 },
        { "id": "O3", "delivery_x": 10, "delivery_y": 8, "deadline": 30, "package_weight": 4 },
        { "id": "O4", "delivery_x": 15, "delivery_y": 10, "deadline": 35, "package_weight": 8 }
    ]
}
```

---

## 📜 How Orders Are Assigned
- Orders are **sorted by nearest location first**, then by **earliest deadline**.
- A drone can **carry multiple orders** if:
  - The **combined weight is within its payload limit**.
  - The **total travel distance is within its range**.
  - The **delivery time of the last order meets the deadline**.
- The drone follows a **continuous optimized path** instead of returning to `(0,0)` after each delivery.

---

## 📏 Formulas Used
### **Manhattan Distance Calculation**
```math
Distance = |x2 - x1| + |y2 - y1|
```

### **Time Calculation**
```math
Time (sec) = Distance / Speed
Time (min) = (Time (sec)) / 60
```

### **Total Distance Calculation**
```math
Total Distance = Delivery Distance + Return Distance
```

---

## 📊 Example Output JSON (`output.json`)
```json
{
    "assignments": [
        {
            "drone": "D1",
            "orders": [
                { "order": "O1", "time_taken": 3.33, "distance": 10 },
                { "order": "O2", "time_taken": 5.33, "distance": 6 },
                { "order": "O3", "time_taken": 8.00, "distance": 8 },
                { "order": "O4", "time_taken": 10.33, "distance": 7 }
            ],
            "total_time": 18.67,
            "total_distance": 56
        }
    ]
}
```



