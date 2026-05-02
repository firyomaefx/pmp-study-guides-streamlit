def calculate_score(correct: int, total: int) -> float:
    """Calculate percentage score"""
    if total == 0:
        return 0.0
    return round((correct / total) * 100, 1)

def is_passing(score: float, threshold: float = 61.5) -> bool:
    """
    Check if score meets passing threshold.
    
    PMI doesn't publish exact passing scores, but industry consensus:
    - ~61.5% (107/175 scored questions)
    - Must pass all three domains (no specific domain fail threshold published)
    """
    return score >= threshold

def domain_breakdown(answers: list) -> dict:
    """
    Break down answers by domain.
    
    Current PMP domains:
    - people: 42% (76 questions)
    - process: 50% (90 questions)  
    - business_environment: 8% (14 questions)
    
    Args:
        answers: List of dicts with 'domain', 'correct' keys
    
    Returns:
        Dict with domain stats: {domain: {'correct': int, 'total': int, 'pct': float}}
    """
    breakdown = {}
    
    for answer in answers:
        domain = answer.get('domain', 'unknown')
        correct = answer.get('correct', False)
        
        if domain not in breakdown:
            breakdown[domain] = {'correct': 0, 'total': 0, 'pct': 0.0}
        
        breakdown[domain]['total'] += 1
        if correct:
            breakdown[domain]['correct'] += 1
    
    # Calculate percentages
    for domain in breakdown:
        total = breakdown[domain]['total']
        if total > 0:
            breakdown[domain]['pct'] = round(
                (breakdown[domain]['correct'] / total) * 100, 1
            )
    
    return breakdown

def format_time(seconds: int) -> str:
    """Format seconds as HH:MM:SS"""
    hours = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{mins:02d}:{secs:02d}"

def get_question_timing_guide() -> dict:
    """
    Return recommended timing per section of the exam
    """
    return {
        "total_time": 230,  # minutes
        "total_questions": 180,
        "time_per_question": 76.7,  # seconds
        "recommended_breaks": [
            {"after_question": 60, "duration": 5},
            {"after_question": 120, "duration": 5}
        ],
        "domain_time_allocations": {
            "people": 97,  # 42% of 230 min
            "process": 115,  # 50% of 230 min
            "business_environment": 18  # 8% of 230 min
        }
    }
