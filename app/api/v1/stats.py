from fastapi import APIRouter, HTTPException
import pandas as pd
from pathlib import Path

router = APIRouter()

base_dir = Path(__file__).parent.parent.parent.parent
height_file = base_dir / "data" / "heights.csv"
weight_file = base_dir / "data" / "weights.csv"


@router.get("/height")
def get_height_stats():
    try:
        df = pd.read_csv(height_file)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=404, detail="File is empty")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


@router.get("/weight")
def get_weight_stats():
    try:
        df = pd.read_csv(weight_file)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=404, detail="File is empty")
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
