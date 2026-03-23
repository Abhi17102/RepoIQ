import os
from dotenv import load_dotenv
import psycopg2
import json
from datetime import datetime

load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        host ="localhost",
        database ="repoiq",
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )
    return conn

def get_cached_user(username):
    conn = get_connection()
    cursor= conn.cursor()
    query = """
    SELECT repo_count, analysis, skills
    FROM github_cache
    WHERE username = %s
    """
    cursor.execute(query, (username,))

    result = cursor.fetchone()

    conn.close()

    if result:
        repo_count, analysis, skills = result

        return {
            "repo_count":repo_count,
            "analysis": analysis,
            "skills": skills
        }
    
    return None

def save_cached_user(username, repo_count, analysis, skills):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO github_cache (username, repo_count, analysis, skills, cached_at)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (username)
    DO UPDATE SET
        repo_count = EXCLUDED.repo_count,
        analysis = EXCLUDED.analysis,
        skills = EXCLUDED.skills,
        cached_at = EXCLUDED.cached_at
    """

    cursor.execute(
        query,
        (
            username,
            repo_count,
            json.dumps(analysis),
            json.dumps(skills),
            datetime.now()
        )
    )

    conn.commit()
    conn.close()
