import requests
import json
import os
import pandas as pd
import sqlite3
import time

def collect_nemo_data():
    # API 요청 URL
    url = "https://www.nemoapp.kr/api/store/search-list"
    
    # 헤더 정보
    headers = {
        "referer": "https://www.nemoapp.kr/store",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }
    
    all_items = []
    page_index = 0
    
    print(f"네모 전체 데이터 수집 시작: {url}")
    
    try:
        while True:
            # 쿼리 파라미터 업데이트
            params = {
                "Subway": "222",
                "Radius": "1000",
                "CompletedOnly": "false",
                "NELat": "37.524082652435375",
                "NELng": "127.04633639319073",
                "SWLat": "37.471760955370655",
                "SWLng": "127.00886288970709",
                "Zoom": "17",
                "SortBy": "29",
                "PageIndex": str(page_index)
            }
            
            print(f"페이지 {page_index} 호출 중...", end="\r")
            
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            items = data.get("items", [])
            
            if not items:
                print(f"\n더 이상 수집할 데이터가 없습니다. (최종 페이지: {page_index-1 if page_index > 0 else 0})")
                break
            
            all_items.extend(items)
            page_index += 1
            
            # 서버 부하 방지를 위한 짧은 지연 시간 (0.5초)
            time.sleep(0.5)
            
        if not all_items:
            print("수집된 데이터가 전혀 없습니다.")
            return

        print(f"총 {len(all_items)}개의 아이템을 수집했습니다.")
        
        # 데이터프레임 변환 (평탄화)
        df = pd.DataFrame(all_items)
        
        # 리스트 형태의 컬럼 처리 (문자열로 변환)
        for col in df.columns:
            if df[col].apply(lambda x: isinstance(x, list)).any():
                df[col] = df[col].apply(lambda x: ", ".join(map(str, x)) if isinstance(x, list) else x)
        
        # 저장 경로 설정
        output_dir = "data"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # 1. JSON 저장
        json_path = os.path.join(output_dir, "nemo_items.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(all_items, f, ensure_ascii=False, indent=4)
            
        # 2. CSV 저장
        csv_path = os.path.join(output_dir, "nemo_items.csv")
        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        
        # 3. Excel 저장
        xlsx_path = os.path.join(output_dir, "nemo_items.xlsx")
        df.to_excel(xlsx_path, index=False)
        
        # 4. SQLite DB 저장
        db_path = os.path.join(output_dir, "nemo_items.db")
        with sqlite3.connect(db_path) as conn:
            df.to_sql("items", conn, if_exists="replace", index=False)
        
        print(f"\n데이터가 다음 경로에 저장되었습니다:")
        print(f"- JSON: {json_path}")
        print(f"- CSV: {csv_path}")
        print(f"- Excel: {xlsx_path}")
        print(f"- SQLite DB: {db_path}")
        
    except Exception as e:
        print(f"\n데이터 수집 및 처리 중 오류 발생: {e}")

if __name__ == "__main__":
    collect_nemo_data()
