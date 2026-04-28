import pandas as pd
import sqlite3
import json
import os

def build_dashboard_data():
    # 1. 데이터 로드
    conn = sqlite3.connect('data/nemo_items.db')
    df = pd.read_sql('SELECT * FROM items', conn)
    conn.close()

    # 2. 요약 데이터 생성
    # 데이터의 가격 단위는 '천 원'임 (예: 5500 = 550만 원)
    summary = {
        "total_items": int(len(df)),
        "avg_deposit": round(float(df['deposit'].mean()) * 1000, 0), # 원 단위로 변환
        "avg_rent": round(float(df['monthlyRent'].mean()), 0), # 만원 단위로 표시할 때 사용
        "avg_maintenance": round(float(df['maintenanceFee'].mean()), 0),
        
        # 업종별 분포 (상위 10개)
        "biz_distribution": df['businessLargeCodeName'].value_counts().head(10).to_dict(),
        
        # 역세권별 분포 (상위 10개)
        "station_distribution": df['nearSubwayStation'].value_counts().head(10).to_dict(),
        
        # 가격대별 분포 (월세 기준, 단위: 만원)
        "rent_bins": pd.cut(df['monthlyRent'] / 10, bins=[0, 100, 300, 500, 1000, 2000, 10000], 
                           labels=['100만 이하', '100-300만', '300-500만', '500-1000만', '1000-2000만', '2000만 초과']).value_counts().to_dict(),
                           
        # 층수별 분포
        "floor_distribution": df['floor'].value_counts().head(10).to_dict(),
        
        # 최근 등록 현황 (요일별)
        "day_distribution": pd.to_datetime(df['createdDateUtc'], format='ISO8601').dt.day_name().value_counts().to_dict()
    }

    # 3. JSON 저장
    output_path = "data/dashboard_summary.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=4)
    
    print(f"대시보드 요약 데이터 생성 완료: {output_path}")

if __name__ == "__main__":
    build_dashboard_data()
