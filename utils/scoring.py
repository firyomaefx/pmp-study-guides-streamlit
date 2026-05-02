def calculate_score(correct: int, total: int) -> float:
    """Calculate percentage score"""
    if total == 0:
        return 0.0
    return round((correct / total) * 100, 1)

def is_passing(score: float, threshold: float = 65.0) -> bool:
    """Check if score meets passing threshold"""
    return score >= threshold

def domain_breakdown(answers: list) -> dict:
    """
    Break down answers by domain.
    
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
    """Format seconds as MM:SS"""
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02d}:{secs:02d}"
