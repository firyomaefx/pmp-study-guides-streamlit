FLASHCARDS = [
  {
    "id": "FC001",
    "category": "terms",
    "knowledge_area": "integration-management",
    "term": "Project Charter",
    "definition": "A document issued by the project initiator or sponsor that formally authorizes the existence of a project and provides the project manager with the authority to apply organizational resources to project activities.",
    "example": "The sponsor signs the project charter, giving the PM authority to spend $500K and hire team members.",
    "memory_tip": "Think of it as the PM's 'license to lead' — no charter, no authority!",
    "related_terms": ["sponsor", "project manager", "authority"]
  },
  {
    "id": "FC002",
    "category": "terms",
    "knowledge_area": "integration-management",
    "term": "Project Management Plan",
    "definition": "A document that defines how the project is executed, monitored, and controlled. It integrates all subsidiary management plans and baselines.",
    "example": "The PM plan includes scope, schedule, cost, quality, resource, communications, risk, procurement, and stakeholder plans.",
    "memory_tip": "It's the PM's 'master playbook' — everything in one place.",
    "related_terms": ["baseline", "subsidiary plan", "integrated"]
  },
  {
    "id": "FC003",
    "category": "terms",
    "knowledge_area": "integration-management",
    "term": "Change Control Board (CCB)",
    "definition": "A formally chartered group responsible for reviewing, evaluating, approving, delaying, or rejecting changes to the project, and for recording and communicating decisions.",
    "example": "The CCB meets weekly to review all change requests over $10K impact.",
    "memory_tip": "CCB = Change Cops Board — they guard the baselines!",
    "related_terms": ["change request", "baseline", "approval"]
  },
  {
    "id": "FC004",
    "category": "terms",
    "knowledge_area": "scope-management",
    "term": "Work Breakdown Structure (WBS)",
    "definition": "A hierarchical decomposition of the total scope of work to be carried out by the project team to accomplish the project objectives and create the required deliverables.",
    "example": "Level 1: Project → Level 2: Design, Build, Test → Level 3: Work packages",
    "memory_tip": "WBS = Work Breakdown into Smaller pieces. 100% rule: if it's not in the WBS, it's not in scope!",
    "related_terms": ["decomposition", "work package", "100% rule"]
  },
  {
    "id": "FC005",
    "category": "terms",
    "knowledge_area": "scope-management",
    "term": "Scope Creep",
    "definition": "The uncontrolled expansion to product or project scope without adjustments to time, cost, and resources.",
    "example": "The client keeps adding 'small' features that weren't in the original requirements.",
    "memory_tip": "Scope Creep is like a weed — it grows unnoticed until it chokes the project!",
    "related_terms": ["gold plating", "change control", "requirements"]
  },
  {
    "id": "FC006",
    "category": "terms",
    "knowledge_area": "scope-management",
    "term": "Gold Plating",
    "definition": "Giving the customer more than what was requested or adding extra features not in scope, often with good intentions.",
    "example": "The team adds a fancy dashboard that wasn't in the requirements because they thought the user would love it.",
    "memory_tip": "Gold plating = 'Look at this shiny extra!' — but it's still scope creep in disguise.",
    "related_terms": ["scope creep", "extras", "customer satisfaction"]
  },
  {
    "id": "FC007",
    "category": "terms",
    "knowledge_area": "schedule-management",
    "term": "Critical Path",
    "definition": "The sequence of activities that represents the longest path through a project, which determines the shortest possible project duration.",
    "example": "If the critical path is 45 days, the project cannot finish sooner than 45 days without crashing or fast-tracking.",
    "memory_tip": "Critical Path = the 'bottleneck chain' — delay any link, and the whole project slips!",
    "related_terms": ["float", "slack", "fast tracking", "crashing"]
  },
  {
    "id": "FC008",
    "category": "terms",
    "knowledge_area": "schedule-management",
    "term": "Fast Tracking",
    "definition": "A schedule compression technique in which activities or phases normally done in sequence are performed in parallel for at least a portion of their duration.",
    "example": "Design and construction overlap — start building the foundation while finalizing upper floor designs.",
    "memory_tip": "Fast Tracking = doing things in parallel that are normally sequential. Risky but fast!",
    "related_terms": ["crashing", "parallel", "risk"]
  },
  {
    "id": "FC009",
    "category": "terms",
    "knowledge_area": "schedule-management",
    "term": "Crashing",
    "definition": "A technique used to shorten the schedule duration for the least incremental cost by adding resources.",
    "example": "Adding 2 more developers to finish coding 2 weeks earlier, costing an extra $20K.",
    "memory_tip": "Crashing = throwing money/resources at the problem to go faster. Always increases cost!",
    "related_terms": ["fast tracking", "resources", "cost increase"]
  },
  {
    "id": "FC010",
    "category": "terms",
    "knowledge_area": "cost-management",
    "term": "Earned Value (EV)",
    "definition": "The measure of work performed expressed in terms of the budget authorized for that work.",
    "example": "If 50% of a $200K project is complete, EV = $100K.",
    "memory_tip": "EV = What you EARNED for the work DONE. Budgeted cost of work performed.",
    "related_terms": ["PV", "AC", "CPI", "SPI"]
  },
  {
    "id": "FC011",
    "category": "formula",
    "knowledge_area": "cost-management",
    "term": "Cost Variance (CV)",
    "definition": "The amount of budget deficit or surplus at a given point in time.",
    "formula": "CV = EV - AC",
    "example": "If EV = $100K and AC = $120K, then CV = -$20K (over budget)",
    "memory_tip": "CV measures Cost performance. Positive = good (under budget), Negative = bad (over budget)",
    "related_terms": ["EV", "AC", "CPI", "cost performance"]
  },
  {
    "id": "FC012",
    "category": "formula",
    "knowledge_area": "cost-management",
    "term": "Schedule Variance (SV)",
    "definition": "The amount by which the project is ahead or behind the planned delivery date.",
    "formula": "SV = EV - PV",
    "example": "If EV = $100K and PV = $90K, then SV = +$10K (ahead of schedule)",
    "memory_tip": "SV measures Schedule performance. Positive = ahead, Negative = behind. Same pattern as CV!",
    "related_terms": ["EV", "PV", "SPI", "schedule performance"]
  },
  {
    "id": "FC013",
    "category": "formula",
    "knowledge_area": "cost-management",
    "term": "Cost Performance Index (CPI)",
    "definition": "A measure of the cost efficiency of budgeted resources expressed as a ratio of earned value to actual cost.",
    "formula": "CPI = EV / AC",
    "example": "If EV = $100K and AC = $120K, CPI = 0.83 (spending $1.20 for every $1.00 of work)",
    "memory_tip": "CPI > 1.0 = good (under budget), CPI < 1.0 = bad (over budget). Think: 'Cost Per Investment'",
    "related_terms": ["EV", "AC", "CV", "EAC"]
  },
  {
    "id": "FC014",
    "category": "formula",
    "knowledge_area": "cost-management",
    "term": "Schedule Performance Index (SPI)",
    "definition": "A measure of schedule efficiency expressed as a ratio of earned value to planned value.",
    "formula": "SPI = EV / PV",
    "example": "If EV = $100K and PV = $90K, SPI = 1.11 (11% ahead of schedule)",
    "memory_tip": "SPI > 1.0 = ahead of schedule, SPI < 1.0 = behind schedule. Same logic as CPI!",
    "related_terms": ["EV", "PV", "SV", "schedule"]
  },
  {
    "id": "FC015",
    "category": "formula",
    "knowledge_area": "cost-management",
    "term": "Estimate at Completion (EAC)",
    "definition": "The expected total cost of completing all work expressed as the sum of the actual cost to date and the estimate to complete.",
    "formula": "EAC = BAC / CPI (if current trends continue)",
    "example": "If BAC = $200K and CPI = 0.8, EAC = $250K (project will cost $250K total)",
    "memory_tip": "EAC = 'Estimate At Completion' — where will we end up? BAC divided by cost performance.",
    "related_terms": ["BAC", "CPI", "ETC", "forecasting"]
  },
  {
    "id": "FC016",
    "category": "formula",
    "knowledge_area": "cost-management",
    "term": "Estimate to Complete (ETC)",
    "definition": "The expected cost to finish all the remaining project work.",
    "formula": "ETC = EAC - AC",
    "example": "If EAC = $250K and AC = $100K, ETC = $150K (need $150K more to finish)",
    "memory_tip": "ETC = 'Estimate To Complete' — how much MORE money do we need? EAC minus what we already spent.",
    "related_terms": ["EAC", "AC", "BAC", "forecasting"]
  },
  {
    "id": "FC017",
    "category": "formula",
    "knowledge_area": "cost-management",
    "term": "To-Complete Performance Index (TCPI)",
    "definition": "A measure of the cost performance that must be achieved with the remaining resources to meet a specified management goal.",
    "formula": "TCPI = (BAC - EV) / (BAC - AC)",
    "example": "If BAC = $200K, EV = $80K, AC = $100K: TCPI = $120K / $100K = 1.2 (must be 20% more efficient)",
    "memory_tip": "TCPI = 'To-Complete Performance Index' — how efficient must we be for the REST of the project? >1.0 means work harder!",
    "related_terms": ["BAC", "EV", "AC", "performance"]
  },
  {
    "id": "FC018",
    "category": "formula",
    "knowledge_area": "cost-management",
    "term": "Variance at Completion (VAC)",
    "definition": "A projection of the amount of budget deficit or surplus, expressed as the difference between the budget at completion and the estimate at completion.",
    "formula": "VAC = BAC - EAC",
    "example": "If BAC = $200K and EAC = $250K, VAC = -$50K (will be $50K over budget)",
    "memory_tip": "VAC = 'Variance At Completion' — will we be over or under budget at the end? Negative = bad (over budget).",
    "related_terms": ["BAC", "EAC", "budget", "forecast"]
  },
  {
    "id": "FC019",
    "category": "formula",
    "knowledge_area": "communications-management",
    "term": "Communication Channels",
    "definition": "The number of potential communication paths between stakeholders in a project.",
    "formula": "n(n-1)/2",
    "example": "With 10 stakeholders: 10 × 9 / 2 = 45 communication channels",
    "memory_tip": "n(n-1)/2 = 'n choose 2' combination formula. Every person talks to every other person. Don't forget to count the PM!",
    "related_terms": ["stakeholders", "communications", "network"]
  },
  {
    "id": "FC020",
    "category": "formula",
    "knowledge_area": "schedule-management",
    "term": "PERT Weighted Average",
    "definition": "A technique used to estimate activity duration by using optimistic, most likely, and pessimistic estimates.",
    "formula": "(Optimistic + 4×Most Likely + Pessimistic) / 6",
    "example": "If O=5 days, M=8 days, P=15 days: (5 + 32 + 15) / 6 = 52/6 = 8.67 days",
    "memory_tip": "PERT = 'Probably Estimate with Realistic Thinking' — weighted toward the most likely, but considers best and worst cases.",
    "related_terms": ["estimate", "duration", "three-point estimating"]
  },
  {
    "id": "FC021",
    "category": "itto",
    "knowledge_area": "integration-management",
    "term": "Inputs to Develop Project Charter",
    "definition": "Business documents, agreements, EEFs, and OPAs are the key inputs for creating the project charter.",
    "example": "Business case proves the project's value; agreements define contracts or MOUs.",
    "memory_tip": "Think 'BEAO' — Business documents, Enterprise factors, Agreements, Organizational assets.",
    "related_terms": ["business case", "agreements", "EEF", "OPA"]
  },
  {
    "id": "FC022",
    "category": "itto",
    "knowledge_area": "integration-management",
    "term": "Outputs of Develop Project Charter",
    "definition": "The project charter and the assumption log are the primary outputs.",
    "example": "Charter authorizes the PM; assumption log records assumptions made during initiation.",
    "memory_tip": "Outputs = Charter + Assumptions. 'C' for Charter, 'A' for Assumptions. CA!",
    "related_terms": ["charter", "assumption log", "authorization"]
  },
  {
    "id": "FC023",
    "category": "itto",
    "knowledge_area": "integration-management",
    "term": "Tools for Perform Integrated Change Control",
    "definition": "Expert judgment, change control tools, data analysis, decision making, and meetings.",
    "example": "The CCB uses voting (decision making) and reviews change impact (data analysis).",
    "memory_tip": "EDDM — Expert judgment, Decision making, Data analysis, Meetings. 'Every Decision Demands Meetings'",
    "related_terms": ["CCB", "change control", "approval"]
  },
  {
    "id": "FC024",
    "category": "itto",
    "knowledge_area": "scope-management",
    "term": "Inputs to Create WBS",
    "definition": "Scope management plan, project scope statement, and requirements documentation.",
    "example": "The scope statement defines what to build; the WBS breaks it down into work packages.",
    "memory_tip": "Inputs = Plan + Statement + Requirements. 'PSR' — Plan, Statement, Requirements.",
    "related_terms": ["WBS", "scope statement", "requirements"]
  },
  {
    "id": "FC025",
    "category": "itto",
    "knowledge_area": "scope-management",
    "term": "Tools for Define Scope",
    "definition": "Expert judgment, data analysis (alternatives analysis), decision making (multi-criteria decision analysis), interpersonal skills, and product analysis.",
    "example": "Product analysis breaks down the product to understand its components and functions.",
    "memory_tip": "EDDIP — Expert, Data analysis, Decision making, Interpersonal, Product analysis. 'Every Detail Demands Important Planning'",
    "related_terms": ["scope", "product analysis", "alternatives"]
  },
  {
    "id": "FC026",
    "category": "process",
    "knowledge_area": "integration-management",
    "term": "Direct and Manage Project Work",
    "definition": "The process of leading and performing the work defined in the project management plan and implementing approved changes to achieve the project's objectives.",
    "example": "The team executes tasks according to the schedule, produces deliverables, and reports work performance data.",
    "memory_tip": "Direct and Manage = 'Do the work, manage the team, deliver the goods.' This is where execution happens!",
    "related_terms": ["execution", "deliverables", "work performance data"]
  },
  {
    "id": "FC027",
    "category": "process",
    "knowledge_area": "integration-management",
    "term": "Monitor and Control Project Work",
    "definition": "The process of tracking, reviewing, and reporting the overall progress to meet the performance objectives defined in the project management plan.",
    "example": "The PM compares actual progress to the baseline, identifies variances, and generates work performance reports.",
    "memory_tip": "Monitor and Control = 'Watch what happens, compare to plan, sound the alarm when things go wrong.'",
    "related_terms": ["variance", "baseline", "work performance reports"]
  },
  {
    "id": "FC028",
    "category": "process",
    "knowledge_area": "scope-management",
    "term": "Collect Requirements",
    "definition": "The process of determining, documenting, and managing stakeholder needs and requirements to meet project objectives.",
    "example": "Interviews, surveys, workshops, and prototypes help capture what stakeholders truly need.",
    "memory_tip": "Collect Requirements = 'Ask, listen, document, verify.' If you don't capture it now, you'll pay for it later!",
    "related_terms": ["requirements", "stakeholder needs", "traceability matrix"]
  },
  {
    "id": "FC029",
    "category": "process",
    "knowledge_area": "scope-management",
    "term": "Validate Scope",
    "definition": "The process of formalizing acceptance of the completed project deliverables.",
    "example": "The customer inspects the finished product and signs off, confirming it meets requirements.",
    "memory_tip": "Validate Scope = 'Customer says YES.' This is external acceptance — Control Quality happens first (internal check).",
    "related_terms": ["acceptance", "deliverables", "control quality"]
  },
  {
    "id": "FC030",
    "category": "process",
    "knowledge_area": "schedule-management",
    "term": "Develop Schedule",
    "definition": "The process of analyzing activity sequences, durations, resource requirements, and schedule constraints to create the project schedule model.",
    "example": "Using CPM and resource leveling to produce a realistic timeline with start and end dates.",
    "memory_tip": "Develop Schedule = 'Put it all together and see how long it really takes.' The output is the project schedule!",
    "related_terms": ["CPM", "resource leveling", "schedule model"]
  },
  {
    "id": "FC031",
    "category": "agile",
    "knowledge_area": "integration-management",
    "term": "Sprint",
    "definition": "A time-boxed iteration in Scrum, typically 1-4 weeks long, where a potentially shippable product increment is created.",
    "example": "The team completes a 2-week sprint, delivering 5 user stories ready for production.",
    "memory_tip": "Sprint = 'Short Race to Produce Increment.' Time-boxed, focused, and ends with a review.",
    "related_terms": ["scrum", "iteration", "time-boxed", "increment"]
  },
  {
    "id": "FC032",
    "category": "agile",
    "knowledge_area": "scope-management",
    "term": "User Story",
    "definition": "A short, simple description of a feature told from the perspective of the user or customer who desires the new capability.",
    "example": "As a project manager, I want to see a dashboard so that I can track project progress easily.",
    "memory_tip": "User Story format: 'As a [role], I want [feature], so that [benefit].' Keep it simple and user-focused!",
    "related_terms": ["backlog", "acceptance criteria", "INVEST"]
  },
  {
    "id": "FC033",
    "category": "agile",
    "knowledge_area": "integration-management",
    "term": "Minimum Viable Product (MVP)",
    "definition": "The version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort.",
    "example": "A startup launches a basic app with only core features to test market demand before building more.",
    "memory_tip": "MVP = 'Minimum features, Maximum learning.' Don't overbuild — test first!",
    "related_terms": ["lean", "validated learning", "product development"]
  },
  {
    "id": "FC034",
    "category": "agile",
    "knowledge_area": "integration-management",
    "term": "Daily Stand-up",
    "definition": "A 15-minute time-boxed event for the Development Team to synchronize activities and create a plan for the next 24 hours.",
    "example": "Team answers: What did I do yesterday? What will I do today? Are there any impediments?",
    "memory_tip": "Stand-up = 'Short, standing, synchronized.' If you're sitting, it's too long!",
    "related_terms": ["scrum", "synchronization", "impediments"]
  },
  {
    "id": "FC035",
    "category": "agile",
    "knowledge_area": "integration-management",
    "term": "Product Backlog",
    "definition": "An ordered list of everything that is known to be needed in the product. It is the single source of requirements for any changes to be made.",
    "example": "Features, bugs, technical debt, and knowledge acquisition items are all in the product backlog.",
    "memory_tip": "Product Backlog = 'The to-do list that never ends.' Constantly refined and reprioritized.",
    "related_terms": ["backlog refinement", "sprint backlog", "prioritization"]
  },
  {
    "id": "FC036",
    "category": "formula",
    "knowledge_area": "cost-management",
    "term": "Planned Value (PV)",
    "definition": "The authorized budget assigned to scheduled work.",
    "formula": "PV = Budgeted cost of work scheduled",
    "example": "By month 3, 30% of work should be done, so PV = 30% of BAC.",
    "memory_tip": "PV = 'Planned Value' — what we PLANNED to have done by now. Budgeted cost of work SCHEDULED.",
    "related_terms": ["BAC", "EV", "schedule baseline"]
  },
  {
    "id": "FC037",
    "category": "formula",
    "knowledge_area": "cost-management",
    "term": "Actual Cost (AC)",
    "definition": "The realized cost incurred for the work performed on an activity during a specific time period.",
    "formula": "AC = Actual cost of work performed",
    "example": "We spent $120K to complete work that was budgeted at $100K.",
    "memory_tip": "AC = 'Actual Cost' — what we ACTUALLY spent. No formula needed, just add up the bills!",
    "related_terms": ["EV", "CPI", "cost baseline"]
  },
  {
    "id": "FC038",
    "category": "terms",
    "knowledge_area": "resource-management",
    "term": "RACI Matrix",
    "definition": "A responsibility assignment matrix that shows the relationship between project activities and team members, using Responsible, Accountable, Consulted, and Informed roles.",
    "example": "For 'Create Design Document': Developer = R, PM = A, Architect = C, Client = I",
    "memory_tip": "RACI = 'Who does what?' R=Responsible (does the work), A=Accountable (owns the decision), C=Consulted (gives input), I=Informed (kept in loop). Only ONE A per task!",
    "related_terms": ["responsibility", "accountability", "matrix"]
  },
  {
    "id": "FC039",
    "category": "terms",
    "knowledge_area": "risk-management",
    "term": "Risk Register",
    "definition": "A document in which the results of risk analysis and risk response planning are recorded.",
    "example": "Lists identified risks, their probability, impact, responses, and owners.",
    "memory_tip": "Risk Register = 'The project's danger diary.' Log it, rate it, plan for it, track it!",
    "related_terms": ["risk analysis", "risk response", "probability", "impact"]
  },
  {
    "id": "FC040",
    "category": "terms",
    "knowledge_area": "risk-management",
    "term": "Monte Carlo Analysis",
    "definition": "A simulation technique that computes the project cost or schedule many times using input values selected at random from probability distributions.",
    "example": "Running 10,000 simulations to determine there's an 80% chance of finishing by June 1st.",
    "memory_tip": "Monte Carlo = 'Roll the dice 10,000 times.' Uses randomness to predict outcomes and probabilities.",
    "related_terms": ["simulation", "probability", "forecasting"]
  },
  {
    "id": "FC041",
    "category": "terms",
    "knowledge_area": "quality-management",
    "term": "Seven Basic Quality Tools",
    "definition": "A set of graphical and statistical tools used to identify and analyze quality problems: cause-and-effect diagrams, flowcharts, checksheets, Pareto diagrams, histograms, control charts, and scatter diagrams.",
    "example": "A Pareto chart shows that 80% of defects come from 20% of causes.",
    "memory_tip": "7 Tools = 'Check the Flow, Histogram, Control, Scatter, Pareto, Cause-and-Effect.' CFHCSP",
    "related_terms": ["quality control", "defects", "analysis"]
  },
  {
    "id": "FC042",
    "category": "terms",
    "knowledge_area": "quality-management",
    "term": "Control Limits vs Specification Limits",
    "definition": "Control limits are boundaries set by the process (3 sigma from mean). Specification limits are boundaries set by the customer/requirements.",
    "example": "Control limits: 98-102 degrees. Specification limits: 95-105 degrees. Process is in control but some outputs may not meet specs.",
    "memory_tip": "Control = process-driven (3σ). Specification = customer-driven. 'Control your process; Specs satisfy the customer.'",
    "related_terms": ["control chart", "specifications", "3 sigma"]
  },
  {
    "id": "FC043",
    "category": "terms",
    "knowledge_area": "stakeholder-management",
    "term": "Stakeholder Analysis",
    "definition": "A technique of systematically gathering and analyzing quantitative and qualitative information to determine whose interests should be taken into account throughout the project.",
    "example": "Power/Interest grid: High Power + High Interest = Manage Closely. Low Power + Low Interest = Monitor.",
    "memory_tip": "Stakeholder Analysis = 'Who matters and how much?' Power + Interest = how to engage them.",
    "related_terms": ["power/interest grid", "engagement", "influence"]
  },
  {
    "id": "FC044",
    "category": "terms",
    "knowledge_area": "communications-management",
    "term": "Communication Methods",
    "definition": "Interactive (real-time dialogue), Push (sent to recipients), and Pull (accessed by recipients on demand).",
    "example": "Interactive = meetings. Push = emails, memos. Pull = intranet, e-learning, shared databases.",
    "memory_tip": "Communication Methods = 'Interact, Push, Pull.' Think: conversation, delivery, self-service.",
    "related_terms": ["interactive", "push", "pull", "communication"]
  },
  {
    "id": "FC045",
    "category": "terms",
    "knowledge_area": "procurement-management",
    "term": "Make-or-Buy Analysis",
    "definition": "A technique used to determine whether a particular product or service can be produced by the project team or should be purchased from an external source.",
    "example": "Should we build our own CRM or buy Salesforce? Compare costs, expertise, and strategic value.",
    "memory_tip": "Make-or-Buy = 'Build it or buy it?' Consider: cost, capacity, control, confidentiality.",
    "related_terms": ["procurement", "outsourcing", "insourcing"]
  },
  {
    "id": "FC046",
    "category": "itto",
    "knowledge_area": "integration-management",
    "term": "Inputs to Close Project",
    "definition": "Project charter, PM plan, project documents, accepted deliverables, business documents, agreements, procurement docs, and OPAs.",
    "example": "Accepted deliverables prove the work is done; procurement docs confirm contracts are closed.",
    "memory_tip": "Close inputs = 'Everything that proves we're done.' Charter (why we started), Deliverables (what we made), Agreements (contracts closed).",
    "related_terms": ["closure", "deliverables", "contracts"]
  },
  {
    "id": "FC047",
    "category": "itto",
    "knowledge_area": "integration-management",
    "term": "Outputs of Close Project",
    "definition": "Project documents updates, final product/service/result transition, final report, and OPAs updates.",
    "example": "Final report summarizes success; lessons learned go to OPA for future projects.",
    "memory_tip": "Close outputs = 'Wrap it up and pass it on.' Final report + Lessons learned = organizational knowledge.",
    "related_terms": ["final report", "lessons learned", "transition"]
  },
  {
    "id": "FC048",
    "category": "itto",
    "knowledge_area": "schedule-management",
    "term": "Tools for Develop Schedule",
    "definition": "Schedule network analysis, critical path method, resource optimization, data analysis, and schedule compression.",
    "example": "CPM identifies the longest path; crashing adds resources; fast tracking overlaps activities.",
    "memory_tip": "Develop Schedule tools = 'Analyze, Optimize, Compress.' AOC — Analyze paths, Optimize resources, Compress duration.",
    "related_terms": ["CPM", "crashing", "fast tracking", "resource leveling"]
  },
  {
    "id": "FC049",
    "category": "process",
    "knowledge_area": "cost-management",
    "term": "Determine Budget",
    "definition": "The process of aggregating the estimated costs of individual activities or work packages to establish an authorized cost baseline.",
    "example": "Sum all work package estimates, add reserves, and get approved as the cost baseline.",
    "memory_tip": "Determine Budget = 'Add it all up and get it approved.' Estimates → Budget → Baseline.",
    "related_terms": ["cost baseline", "estimates", "reserves", "funding"]
  },
  {
    "id": "FC050",
    "category": "agile",
    "knowledge_area": "integration-management",
    "term": "Definition of Done (DoD)",
    "definition": "A shared understanding of what it means for work to be complete, ensuring quality and consistency across increments.",
    "example": "Code reviewed, unit tested, documentation updated, accepted by product owner.",
    "memory_tip": "DoD = 'Done means DONE.' No 'almost done' — everyone agrees on the checklist before starting.",
    "related_terms": ["acceptance", "quality", "sprint"]
  }
]

