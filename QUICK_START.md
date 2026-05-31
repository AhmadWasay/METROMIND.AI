# ⚡ Quick Start (5 Minutes)

## Prerequisites
- Python 3.9+ installed
- Node.js 16+ installed
- 2 terminal windows ready

## Start Backend (Terminal 1)

```bash
cd backend
python -m venv venv
venv\Scripts\activate              # Windows
# source venv/bin/activate        # macOS/Linux

pip install -r requirements.txt
uvicorn main:app --reload
```

Wait for: `Uvicorn running on http://0.0.0.0:8000`

## Start Frontend (Terminal 2)

```bash
cd frontend
npm install
npm start
```

Wait for: `Compiled successfully!`

## Open Browser

http://localhost:3000

## Test It

1. Select: Red Sector G7 → Blue NUST
2. Click: Find Route
3. Click: Order Now
4. Click: View Order

**Done!** 🎉

---

## API Testing (Optional)

Open: http://localhost:8000/docs

Try endpoints:
- `GET /api/stations`
- `POST /api/get-route`
- `POST /api/book-route`
- `GET /api/admin/analytics`

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 8000 taken | `uvicorn main:app --port 8001` |
| "npm not found" | Install Node.js from nodejs.org |
| Map not showing | Refresh page, check console |
| No results | Check station names match |

---

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions.
