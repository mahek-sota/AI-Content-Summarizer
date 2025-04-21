from fastapi import FastAPI, HTTPException
from models import SummaryRequest, SummaryResponse, HistoryResponse
from summarizer.py import summarize_text
from history import save_summary, get_summary_history

app = FastAPI()

@app.post("/summarize", response_model=SummaryResponse)
async def summarize(req: SummaryRequest):
    try:
        summary = await summarize_text(req.content, req.mode)
        save_summary(req.content, summary, req.mode)
        return SummaryResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history", response_model=list[HistoryResponse])
async def get_history():
    return get_summary_history()
