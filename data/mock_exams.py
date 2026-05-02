MOCK_EXAMS = [
  {
    "exam_id": "mock-01",
    "name": "Mock Exam 1 - Foundation",
    "description": "A balanced exam covering all PMP domains with mixed difficulty. Perfect for your first assessment to identify strengths and weaknesses.",
    "duration_minutes": 120,
    "total_questions": 15,
    "passing_score": 65,
    "questions": [
      {
        "id": "M1Q001",
        "domain": "process",
        "knowledge_area": "integration-management",
        "difficulty": "easy",
        "scenario": "A new project has been approved by the portfolio steering committee. The sponsor has assigned you as the project manager.",
        "question": "What is the FIRST thing you should do as the newly assigned project manager?",
        "options": [
          {"id": "A", "text": "Start planning the project schedule"},
          {"id": "B", "text": "Review and obtain the project charter"},
          {"id": "C", "text": "Meet with all stakeholders immediately"},
          {"id": "D", "text": "Begin resource acquisition"}
        ],
        "correct_answer": "B",
        "explanation": "The project charter formally authorizes the project manager and provides the authority to apply organizational resources. Without the charter, the PM has no formal authority. Planning (A), meeting stakeholders (C), and acquiring resources (D) should come after obtaining the charter.",
        "references": ["PMBOK 6th Ed, Section 4.1"]
      },
      {
        "id": "M1Q002",
        "domain": "people",
        "knowledge_area": "resource-management",
        "difficulty": "medium",
        "scenario": "Your project team consists of 8 members from different functional departments. Two senior developers are having frequent disagreements about technical approaches, which is affecting team morale.",
        "question": "As the project manager, what is the MOST appropriate conflict resolution approach to use FIRST?",
        "options": [
          {"id": "A", "text": "Force a decision quickly to maintain schedule"},
          {"id": "B", "text": "Facilitate a discussion to find a collaborative solution"},
          {"id": "C", "text": "Remove both developers from the project"},
          {"id": "D", "text": "Escalate the issue to functional managers immediately"}
        ],
        "correct_answer": "B",
        "explanation": "Collaborating/problem-solving is the preferred conflict resolution approach as it addresses the root cause and builds team cohesion. Forcing (A) may create resentment. Removing team members (C) is extreme and costly. Escalation (D) should be used only when team-level resolution fails.",
        "references": ["PMBOK 6th Ed, Section 9.5"]
      },
      {
        "id": "M1Q003",
        "domain": "process",
        "knowledge_area": "scope-management",
        "difficulty": "medium",
        "scenario": "During a project status meeting, the customer requests an additional feature that was not included in the original requirements documentation.",
        "question": "What should the project manager do FIRST when receiving this request?",
        "options": [
          {"id": "A", "text": "Add the feature to show goodwill to the customer"},
          {"id": "B", "text": "Submit a change request through the Perform Integrated Change Control process"},
          {"id": "C", "text": "Estimate the cost and schedule impact immediately"},
          {"id": "D", "text": "Reject the request since it was not in the original scope"}
        ],
        "correct_answer": "B",
        "explanation": "Any change to scope must go through the Perform Integrated Change Control process. The PM should not add features directly (A = gold plating), estimate before change control (C), or reject without analysis (D). The formal change process ensures proper evaluation of impact.",
        "references": ["PMBOK 6th Ed, Section 4.6"]
      },
      {
        "id": "M1Q004",
        "domain": "business_environment",
        "knowledge_area": "stakeholder-management",
        "difficulty": "easy",
        "scenario": "A project to implement a new ERP system is in the initiation phase. You need to identify all parties who may affect or be affected by the project.",
        "question": "What is the PRIMARY output of the Identify Stakeholders process?",
        "options": [
          {"id": "A", "text": "Stakeholder Engagement Plan"},
          {"id": "B", "text": "Stakeholder Register"},
          {"id": "C", "text": "Communications Management Plan"},
          {"id": "D", "text": "Risk Register"}
        ],
        "correct_answer": "B",
        "explanation": "The Stakeholder Register is the primary output of the Identify Stakeholders process. It documents identified stakeholders and their interests, influence, and impact. The Stakeholder Engagement Plan (A) is an output of Plan Stakeholder Engagement. Communications Management Plan (C) and Risk Register (D) are separate subsidiary plans.",
        "references": ["PMBOK 6th Ed, Section 13.1"]
      },
      {
        "id": "M1Q005",
        "domain": "process",
        "knowledge_area": "cost-management",
        "difficulty": "hard",
        "scenario": "Your project has a Budget at Completion (BAC) of $500,000. At the current status date, Earned Value (EV) is $200,000, Actual Cost (AC) is $250,000, and Planned Value (PV) is $220,000.",
        "question": "If current cost trends continue, what is the Estimate at Completion (EAC)?",
        "options": [
          {"id": "A", "text": "$400,000"},
          {"id": "B", "text": "$500,000"},
          {"id": "C", "text": "$625,000"},
          {"id": "D", "text": "$550,000"}
        ],
        "correct_answer": "C",
        "explanation": "CPI = EV / AC = $200K / $250K = 0.8. If current trends continue, EAC = BAC / CPI = $500K / 0.8 = $625K. This means the project will cost $625K total if performance doesn't improve.",
        "references": ["PMBOK 6th Ed, Section 7.4"]
      },
      {
        "id": "M1Q006",
        "domain": "process",
        "knowledge_area": "schedule-management",
        "difficulty": "medium",
        "scenario": "You are developing the project schedule. Activity A has a duration of 5 days and must finish before Activity B can start. Activity C can start 2 days before Activity A finishes.",
        "question": "What type of dependency exists between Activity A and Activity C?",
        "options": [
          {"id": "A", "text": "Finish-to-Start (FS)"},
          {"id": "B", "text": "Start-to-Start (SS)"},
          {"id": "C", "text": "Finish-to-Finish (FF)"},
          {"id": "D", "text": "Start-to-Finish (SF)"}
        ],
        "correct_answer": "A",
        "explanation": "Activity C can start 2 days before Activity A finishes with a 2-day lead. This is a Finish-to-Start (FS) relationship with a lead time. The basic relationship is FS, modified by the lead.",
        "references": ["PMBOK 6th Ed, Section 6.3"]
      },
      {
        "id": "M1Q007",
        "domain": "people",
        "knowledge_area": "communications-management",
        "difficulty": "easy",
        "scenario": "Your project has 12 stakeholders including you as the project manager.",
        "question": "How many potential communication channels exist in this project?",
        "options": [
          {"id": "A", "text": "12"},
          {"id": "B", "text": "66"},
          {"id": "C", "text": "132"},
          {"id": "D", "text": "24"}
        ],
        "correct_answer": "B",
        "explanation": "Communication channels formula: n(n-1)/2 where n = number of stakeholders. With 12 stakeholders: 12 × 11 / 2 = 66 channels. Don't forget to count the project manager in the total!",
        "references": ["PMBOK 6th Ed, Section 10.2"]
      },
      {
        "id": "M1Q008",
        "domain": "process",
        "knowledge_area": "quality-management",
        "difficulty": "medium",
        "scenario": "During quality control inspections, you notice that defects are consistently occurring in the same component. You need to identify the root cause of these defects.",
        "question": "Which quality tool is BEST suited for identifying the root cause of these defects?",
        "options": [
          {"id": "A", "text": "Pareto Chart"},
          {"id": "B", "text": "Cause-and-Effect Diagram (Fishbone)"},
          {"id": "C", "text": "Control Chart"},
          {"id": "D", "text": "Histogram"}
        ],
        "correct_answer": "B",
        "explanation": "The Cause-and-Effect Diagram (also called Fishbone or Ishikawa) is specifically designed to identify root causes by categorizing potential causes. Pareto Chart (A) shows which defects occur most frequently. Control Chart (C) monitors process stability. Histogram (D) shows frequency distribution.",
        "references": ["PMBOK 6th Ed, Section 8.3"]
      },
      {
        "id": "M1Q009",
        "domain": "business_environment",
        "knowledge_area": "integration-management",
        "difficulty": "medium",
        "scenario": "A project to develop a new mobile banking app is in its final phase. All deliverables have been accepted, contracts have been closed, and lessons learned have been documented.",
        "question": "What should the project manager do LAST when closing this project?",
        "options": [
          {"id": "A", "text": "Release the project team"},
          {"id": "B", "text": "Archive project documents"},
          {"id": "C", "text": "Celebrate success with the team"},
          {"id": "D", "text": "Obtain formal sign-off from the customer"}
        ],
        "correct_answer": "C",
        "explanation": "While celebrating success (C) is important for team morale, it's typically done after administrative closure activities. However, the question asks what should be done LAST. Customer sign-off (D) should occur early in closing. Document archiving (B) and team release (A) are administrative activities. Team celebration is often the final activity to recognize contributions. Note: In the PMP exam, 'release resources' is usually considered the last formal step, but celebrating success is also a closing activity.",
        "references": ["PMBOK 6th Ed, Section 4.7"]
      },
      {
        "id": "M1Q010",
        "domain": "process",
        "knowledge_area": "risk-management",
        "difficulty": "hard",
        "scenario": "Your project team has identified a risk that could cause a 3-week delay if it occurs. The probability of this risk occurring is estimated at 40%.",
        "question": "If the risk occurs, you have identified a contingency reserve of $50,000 to address it. What type of reserve is this?",
        "options": [
          {"id": "A", "text": "Management Reserve"},
          {"id": "B", "text": "Contingency Reserve"},
          {"id": "C", "text": "Cost Baseline"},
          {"id": "D", "text": "Project Budget"}
        ],
        "correct_answer": "B",
        "explanation": "Contingency Reserve is allocated for identified risks that have been analyzed and for which contingent responses are developed. Management Reserve (A) is for unknown unknowns (unidentified risks). Cost Baseline (C) includes the contingency reserve. Project Budget (D) includes both cost baseline and management reserve.",
        "references": ["PMBOK 6th Ed, Section 7.3"]
      },
      {
        "id": "M1Q011",
        "domain": "people",
        "knowledge_area": "integration-management",
        "difficulty": "medium",
        "scenario": "You are managing a hybrid project using both predictive and agile approaches. The team is struggling with transitioning between detailed upfront planning and adaptive iteration planning.",
        "question": "What is the BEST approach to manage planning in this hybrid environment?",
        "options": [
          {"id": "A", "text": "Use only predictive planning for the entire project"},
          {"id": "B", "text": "Use rolling wave planning with detailed near-term and high-level future planning"},
          {"id": "C", "text": "Eliminate all upfront planning and use only iteration planning"},
          {"id": "D", "text": "Maintain two separate plans - one predictive and one agile"}
        ],
        "correct_answer": "B",
        "explanation": "Rolling wave planning is the ideal approach for hybrid environments. It provides detailed planning for near-term work while maintaining high-level plans for future work. This balances the need for structure with the flexibility to adapt. Using only predictive (A) or only agile (C) defeats the purpose of hybrid. Maintaining separate plans (D) creates confusion and duplication.",
        "references": ["PMBOK 7th Ed, Agile Practice Guide"]
      },
      {
        "id": "M1Q012",
        "domain": "process",
        "knowledge_area": "procurement-management",
        "difficulty": "easy",
        "scenario": "Your organization needs to purchase specialized testing equipment for a 6-month project. The equipment will not be needed after the project ends.",
        "question": "What procurement strategy is MOST appropriate for this situation?",
        "options": [
          {"id": "A", "text": "Make - Build the equipment in-house"},
          {"id": "B", "text": "Buy - Lease the equipment for the project duration"},
          {"id": "C", "text": "Share - Partner with another company to co-own the equipment"},
          {"id": "D", "text": "Rent - Purchase the equipment outright"}
        ],
        "correct_answer": "B",
        "explanation": "Leasing (Buy/Acquire) is most appropriate for equipment needed short-term. Building in-house (A) is costly and time-consuming for specialized equipment. Co-ownership (C) is complex for a 6-month need. Purchasing outright (D) is wasteful if the equipment won't be used again.",
        "references": ["PMBOK 6th Ed, Section 12.1"]
      },
      {
        "id": "M1Q013",
        "domain": "process",
        "knowledge_area": "scope-management",
        "difficulty": "medium",
        "scenario": "The project team has completed the WBS and is now estimating the cost of each work package. Some work packages cannot be estimated with precision because detailed information is not yet available.",
        "question": "What estimating technique is MOST appropriate for work packages with limited available information?",
        "options": [
          {"id": "A", "text": "Bottom-up estimating"},
          {"id": "B", "text": "Analogous estimating"},
          {"id": "C", "text": "Parametric estimating"},
          {"id": "D", "text": "Three-point estimating"}
        ],
        "correct_answer": "B",
        "explanation": "Analogous estimating uses historical data from similar projects and is useful when limited information is available. It's less accurate but faster. Bottom-up (A) requires detailed information. Parametric (C) needs statistical relationships. Three-point (D) requires optimistic, pessimistic, and most likely estimates.",
        "references": ["PMBOK 6th Ed, Section 6.4"]
      },
      {
        "id": "M1Q014",
        "domain": "people",
        "knowledge_area": "resource-management",
        "difficulty": "hard",
        "scenario": "A key subject matter expert (SME) on your project has been reassigned to another high-priority project by their functional manager. This SME was critical to the technical design phase starting next week.",
        "question": "What should the project manager do FIRST to address this situation?",
        "options": [
          {"id": "A", "text": "Immediately hire an external consultant as a replacement"},
          {"id": "B", "text": "Negotiate with the functional manager to retain the SME during critical phase"},
          {"id": "C", "text": "Crash the schedule by adding more resources to compensate"},
          {"id": "D", "text": "Submit a change request to extend the project timeline"}
        ],
        "correct_answer": "B",
        "explanation": "The PM should first negotiate with the functional manager (B) since this is a resource conflict that might be resolvable. Hiring externally (A) is costly and may not be necessary. Crashing (C) doesn't solve the expertise gap. Submitting a change request (D) is premature before attempting negotiation.",
        "references": ["PMBOK 6th Ed, Section 9.4"]
      },
      {
        "id": "M1Q015",
        "domain": "business_environment",
        "knowledge_area": "integration-management",
        "difficulty": "medium",
        "scenario": "Your organization is considering two projects. Project A has an NPV of $200,000 over 3 years. Project B has an NPV of $150,000 over 2 years. Both projects have similar risk profiles.",
        "question": "Based on financial analysis, which project should the organization select?",
        "options": [
          {"id": "A", "text": "Project A because it has higher NPV"},
          {"id": "B", "text": "Project B because it has shorter payback period"},
          {"id": "C", "text": "Project A because it has longer duration"},
          {"id": "D", "text": "Cannot determine without IRR information"}
        ],
        "correct_answer": "A",
        "explanation": "When comparing projects with similar risk profiles, the project with the higher NPV (Net Present Value) should be selected. NPV considers the time value of money and provides the absolute value added. Project A has higher NPV ($200K vs $150K), making it the better choice. Payback period (B) doesn't consider total value. Duration (C) is not a selection criterion. IRR (D) is another metric but NPV is sufficient for this decision.",
        "references": ["PMBOK 6th Ed, Section 1.2"]
      }
    ]
  },
  {
    "exam_id": "mock-02",
    "name": "Mock Exam 2 - Process Heavy",
    "description": "Emphasizes Process domain questions (scheduling, cost, quality, procurement). Tests technical knowledge depth with more complex scenarios.",
    "duration_minutes": 120,
    "total_questions": 15,
    "passing_score": 65,
    "questions": [
      {
        "id": "M2Q001",
        "domain": "process",
        "knowledge_area": "cost-management",
        "difficulty": "hard",
        "scenario": "A project has the following earned value data at month 6: BAC = $400,000, EV = $160,000, AC = $200,000, PV = $180,000. The project sponsor wants to know the minimum cost performance efficiency needed for the remaining work to complete within the original budget.",
        "question": "What is the TCPI based on the BAC?",
        "options": [
          {"id": "A", "text": "0.80"},
          {"id": "B", "text": "1.20"},
          {"id": "C", "text": "1.33"},
          {"id": "D", "text": "0.75"}
        ],
        "correct_answer": "B",
        "explanation": "TCPI = (BAC - EV) / (BAC - AC) = ($400K - $160K) / ($400K - $200K) = $240K / $200K = 1.20. The team must work 20% more efficiently than originally planned to finish within budget.",
        "references": ["PMBOK 6th Ed, Section 7.4"]
      },
      {
        "id": "M2Q002",
        "domain": "process",
        "knowledge_area": "schedule-management",
        "difficulty": "hard",
        "scenario": "Your project network diagram shows the following critical path activities: A(3 days) → B(5 days) → C(4 days) → D(6 days). Activity B has a 2-day lead with Activity E, which is on a non-critical path.",
        "question": "If Activity B is delayed by 3 days, what is the impact on the project completion date?",
        "options": [
          {"id": "A", "text": "No impact because Activity E has float"},
          {"id": "B", "text": "3 days delay because B is on the critical path"},
          {"id": "C", "text": "1 day delay because of the lead time"},
          {"id": "D", "text": "5 days delay because of cumulative effect"}
        ],
        "correct_answer": "B",
        "explanation": "Activity B is on the critical path, so any delay to B directly delays the project. A 3-day delay in B results in a 3-day project delay. The lead with Activity E (2 days) doesn't affect the critical path delay. Float on non-critical paths doesn't protect the critical path.",
        "references": ["PMBOK 6th Ed, Section 6.5"]
      },
      {
        "id": "M2Q003",
        "domain": "process",
        "knowledge_area": "quality-management",
        "difficulty": "medium",
        "scenario": "A manufacturing project is producing components with the following specification limits: 95-105 degrees. The control chart shows a process mean of 100 degrees with control limits of 98-102 degrees. The last 5 measurements were: 97, 101, 99, 103, 96.",
        "question": "What should the project manager conclude about this process?",
        "options": [
          {"id": "A", "text": "The process is in control and meeting specifications"},
          {"id": "B", "text": "The process is out of control but meeting specifications"},
          {"id": "C", "text": "The process is out of control and not meeting specifications"},
          {"id": "D", "text": "The process is in control but not meeting specifications"}
        ],
        "correct_answer": "C",
        "explanation": "Two points (103 and 96) are outside the control limits (98-102), so the process is out of control. Additionally, 96 is below the lower specification limit (95), meaning the process is also not meeting specifications. Control limits (process-driven) are tighter than specification limits (customer-driven).",
        "references": ["PMBOK 6th Ed, Section 8.3"]
      },
      {
        "id": "M2Q004",
        "domain": "process",
        "knowledge_area": "procurement-management",
        "difficulty": "medium",
        "scenario": "You are evaluating bids from three vendors for a construction subcontract. Vendor A has the lowest price but limited experience with similar projects. Vendor B has moderate price and excellent references. Vendor C has the highest price but is a long-term partner.",
        "question": "Which vendor selection criteria is MOST appropriate for this decision?",
        "options": [
          {"id": "A", "text": "Lowest price only"},
          {"id": "B", "text": "Multi-criteria decision analysis considering price, experience, and risk"},
          {"id": "C", "text": "Past relationship only"},
          {"id": "D", "text": "Fastest delivery time only"}
        ],
        "correct_answer": "B",
        "explanation": "Multi-criteria decision analysis (MCDA) is the best approach for complex vendor selection. It evaluates multiple factors (price, experience, risk, references) rather than relying on a single criterion. Lowest price (A) ignores risk. Past relationship (C) ignores capability. Delivery time (D) is only one factor.",
        "references": ["PMBOK 6th Ed, Section 12.2"]
      },
      {
        "id": "M2Q005",
        "domain": "process",
        "knowledge_area": "integration-management",
        "difficulty": "hard",
        "scenario": "A project is experiencing significant scope creep due to frequent customer change requests. The project is now 20% over budget and 2 weeks behind schedule. The customer is demanding additional features that were not in the original scope.",
        "question": "What should the project manager do FIRST to regain control of this situation?",
        "options": [
          {"id": "A", "text": "Implement all customer requests to maintain goodwill"},
          {"id": "B", "text": "Conduct a thorough impact analysis and present to the CCB"},
          {"id": "C", "text": "Crash the schedule by adding more resources"},
          {"id": "D", "text": "Terminate the project to avoid further losses"}
        ],
        "correct_answer": "B",
        "explanation": "The PM must first analyze the impact of changes and present to the Change Control Board (CCB). This establishes formal change control. Implementing all requests (A) worsens the problem. Crashing (C) is a response, not a first step. Termination (D) is premature without analysis.",
        "references": ["PMBOK 6th Ed, Section 4.6"]
      }
    ]
  },
  {
    "exam_id": "mock-03",
    "name": "Mock Exam 3 - Agile & Hybrid",
    "description": "Focuses on agile methodologies, hybrid approaches, adaptive environments, and Scrum practices. Tests modern project management approaches.",
    "duration_minutes": 120,
    "total_questions": 15,
    "passing_score": 65,
    "questions": [
      {
        "id": "M3Q001",
        "domain": "people",
        "knowledge_area": "integration-management",
        "difficulty": "medium",
        "scenario": "A Scrum team has been working on a product for 3 sprints. The product owner is concerned that the team is not delivering enough value each sprint.",
        "question": "What is the BEST way for the Product Owner to measure value delivery in Scrum?",
        "options": [
          {"id": "A", "text": "Count the number of user stories completed per sprint"},
          {"id": "B", "text": "Track velocity and measure business value per story point"},
          {"id": "C", "text": "Compare actual hours worked vs. estimated hours"},
          {"id": "D", "text": "Monitor individual developer productivity"}
        ],
        "correct_answer": "B",
        "explanation": "Velocity measures the amount of work completed, and business value per story point measures value delivery. Counting stories (A) ignores size differences. Tracking hours (C) measures effort, not value. Individual productivity (D) contradicts Scrum's team-focused approach.",
        "references": ["Agile Practice Guide, Scrum Guide"]
      },
      {
        "id": "M3Q002",
        "domain": "people",
        "knowledge_area": "scope-management",
        "difficulty": "easy",
        "scenario": "A team is refining user stories for the upcoming sprint. The product owner has provided initial descriptions but the team is unsure about the acceptance criteria.",
        "question": "Who is responsible for defining and clarifying acceptance criteria for user stories?",
        "options": [
          {"id": "A", "text": "The Scrum Master"},
          {"id": "B", "text": "The Product Owner"},
          {"id": "C", "text": "The Development Team"},
          {"id": "D", "text": "The Project Manager"}
        ],
        "correct_answer": "B",
        "explanation": "The Product Owner is responsible for defining acceptance criteria that clarify what 'done' means for each user story. While the team (C) collaborates on refining stories, the PO owns the criteria. Scrum Master (A) facilitates but doesn't define. Project Manager (D) is not a Scrum role.",
        "references": ["Scrum Guide"]
      },
      {
        "id": "M3Q003",
        "domain": "people",
        "knowledge_area": "integration-management",
        "difficulty": "medium",
        "scenario": "A hybrid project is using predictive planning for the foundation phase and adaptive approaches for the software development phase. The team is transitioning from detailed upfront design to iterative development.",
        "question": "What is the BIGGEST risk when transitioning from predictive to adaptive approaches within the same project?",
        "options": [
          {"id": "A", "text": "Increased documentation requirements"},
          {"id": "B", "text": "Confusion about accountability and decision-making authority"},
          {"id": "C", "text": "Reduced team collaboration"},
          {"id": "D", "text": "Slower delivery of working software"}
        ],
        "correct_answer": "B",
        "explanation": "The biggest risk is confusion about roles, accountability, and decision-making when shifting between predictive (PM-driven) and adaptive (team-driven) approaches. Documentation (A) typically decreases in adaptive. Collaboration (C) increases in adaptive. Delivery speed (D) often improves with adaptive.",
        "references": ["Agile Practice Guide, PMBOK 7th Ed"]
      },
      {
        "id": "M3Q004",
        "domain": "business_environment",
        "knowledge_area": "integration-management",
        "difficulty": "hard",
        "scenario": "An organization is deciding between three projects using agile approaches:\n\nProject X: 6 sprints, estimated value $300K, team velocity 30 points/sprint\nProject Y: 4 sprints, estimated value $200K, team velocity 25 points/sprint\nProject Z: 8 sprints, estimated value $400K, team velocity 35 points/sprint",
        "question": "Which project provides the BEST value per sprint based on this information?",
        "options": [
          {"id": "A", "text": "Project X ($50K value per sprint)"},
          {"id": "B", "text": "Project Y ($50K value per sprint)"},
          {"id": "C", "text": "Project Z ($50K value per sprint)"},
          {"id": "D", "text": "All projects provide equal value per sprint"}
        ],
        "correct_answer": "D",
        "explanation": "Project X: $300K / 6 = $50K per sprint. Project Y: $200K / 4 = $50K per sprint. Project Z: $400K / 8 = $50K per sprint. All three projects provide equal value per sprint ($50K). However, Project Z delivers the most total value ($400K) but takes the longest. The decision should consider strategic alignment, risk, and organizational capacity.",
        "references": ["Agile Practice Guide"]
      }
    ]
  }
]

