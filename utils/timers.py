import time
import streamlit as st

def get_exam_duration_minutes() -> int:
    """Return official PMP exam duration in minutes"""
    return 230  # 3 hours 50 minutes

def get_exam_total_questions() -> int:
    """Return official PMP exam total questions"""
    return 180  # 175 scored + 5 unscored/pretest

def get_passing_threshold() -> float:
    """Return passing score percentage"""
    return 61.5  # ~107/175 correct (PMI doesn't publish exact %)

def format_duration(minutes: int) -> str:
    """Format minutes into hours and minutes"""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}h {mins}m"

def get_domain_breakdown() -> dict:
    """
    Return current PMP exam domain weightings.
    
    Current (before July 2026):
    - People: 42%
    - Process: 50%
    - Business Environment: 8%
    
    New (July 2026+):
    - People: 33%
    - Process: 41%
    - Business Environment: 26%
    """
    return {
        "current": {
            "people": {"pct": 42, "questions": 76, "description": "Leadership, team performance, conflict management, stakeholder engagement"},
            "process": {"pct": 50, "questions": 90, "description": "Technical project management, integration, scope, schedule, cost, quality"},
            "business_environment": {"pct": 8, "questions": 14, "description": "Strategy alignment, benefits realization, compliance, governance"}
        },
        "july_2026": {
            "people": {"pct": 33, "questions": 59, "description": "Leadership, team performance, stakeholder engagement (reduced focus)"},
            "process": {"pct": 41, "questions": 74, "description": "Technical PM, integration, scope, schedule, cost, quality (reduced)"},
            "business_environment": {"pct": 26, "questions": 47, "description": "Strategy, benefits, compliance, AI impact, sustainability (major increase)"}
        }
    }

def get_question_type_breakdown() -> dict:
    """Return PMP exam question type distribution"""
    return {
        "multiple_choice": {"pct": 85, "description": "Standard multiple choice with 4 options"},
        "multiple_select": {"pct": 10, "description": "Select multiple correct answers"},
        "matching": {"pct": 3, "description": "Match items from two columns"},
        "hotspot": {"pct": 2, "description": "Click on correct area of image/diagram"}
    }

def get_exam_tips() -> list:
    """Return official PMP exam tips"""
    return [
        "You have ~76 seconds per question (230 min ÷ 180 questions)",
        "Take 2 breaks during the exam (after 60 and 120 questions)",
        "Answer all questions — there's no penalty for wrong answers",
        "Flag difficult questions and return to them later",
        "Read the last sentence first to understand what is being asked",
        "Look for absolutes like 'always', 'never', 'only' — they're usually wrong",
        "The 'best' answer may not be perfect, but it's the most appropriate",
        "Process questions: identify what process group you're in first",
        "People questions: think about servant leadership and emotional intelligence",
        "Business Environment: focus on strategy alignment and value delivery"
    ]
