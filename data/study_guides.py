STUDY_GUIDES = {}

STUDY_GUIDES['integration-management'] = {
    "id":  "integration-management",
    "name":  "Project Integration Management",
    "description":  "Identify, define, combine, unify, and coordinate the various processes and project management activities within the Project Management Process Groups.",
    "processes":  [
                      {
                          "id":  "4.1",
                          "name":  "Develop Project Charter",
                          "process_group":  "Initiating",
                          "description":  "The process of developing a document that formally authorizes the existence of a project and provides the project manager with the authority to apply organizational resources to project activities.",
                          "inputs":  [
                                         "Business documents (business case, benefits management plan)",
                                         "Agreements",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (brainstorming, focus groups, interviews)",
                                                   "Interpersonal and team skills (conflict management, facilitation, meeting management)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Project charter",
                                          "Assumption log"
                                      ],
                          "exam_traps":  [
                                             "The project charter is issued by the sponsor or PMO — NOT the project manager",
                                             "The charter formally authorizes the PM — without it, the PM has no authority",
                                             "High-level requirements and risks are in the charter, NOT detailed ones"
                                         ],
                          "agile_considerations":  [
                                                       "In agile, the charter may be lighter — but still needs sponsor authorization",
                                                       "Project vision and success criteria are defined upfront even in adaptive environments"
                                                   ]
                      },
                      {
                          "id":  "4.2",
                          "name":  "Develop Project Management Plan",
                          "process_group":  "Planning",
                          "description":  "The process of defining, preparing, and coordinating all plan components and consolidating them into an integrated project management plan.",
                          "inputs":  [
                                         "Project charter",
                                         "Outputs from other processes",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (brainstorming, checklists, focus groups, interviews)",
                                                   "Interpersonal and team skills (conflict management, facilitation, meeting management)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Project management plan",
                                          "Project documents (assumption log, basis of estimates, change log, etc.)"
                                      ],
                          "exam_traps":  [
                                             "The PM plan is a living document — it gets updated, not changed via formal change control",
                                             "Subsidiary plans (scope, schedule, cost, etc.) are part of the PM plan",
                                             "The PM plan CANNOT be changed by the PM alone — it needs CCB approval"
                                         ],
                          "agile_considerations":  [
                                                       "In agile, planning is iterative — rolling wave planning is common",
                                                       "The PM plan may include release plans, iteration plans, and product roadmaps"
                                                   ]
                      },
                      {
                          "id":  "4.3",
                          "name":  "Direct and Manage Project Work",
                          "process_group":  "Executing",
                          "description":  "The process of leading and performing the work defined in the project management plan and implementing approved changes to achieve the project\u0027s objectives.",
                          "inputs":  [
                                         "Project management plan",
                                         "Project documents (change log, lessons learned register, milestone list, etc.)",
                                         "Approved change requests",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Project management information system (PMIS)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Deliverables",
                                          "Work performance data",
                                          "Issue log",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Work performance DATA (raw observations) → Work performance INFORMATION (analyzed) → Work performance REPORTS (presented)",
                                             "Change requests can be corrective, preventive, defect repair, or updates",
                                             "Issue log is created here — log everything and track to closure"
                                         ],
                          "agile_considerations":  [
                                                       "Daily stand-ups help direct and manage work in agile",
                                                       "Team self-organizes to complete backlog items"
                                                   ]
                      },
                      {
                          "id":  "4.4",
                          "name":  "Manage Project Knowledge",
                          "process_group":  "Executing",
                          "description":  "The process of using existing knowledge and creating new knowledge to achieve the project\u0027s objectives and contribute to organizational learning.",
                          "inputs":  [
                                         "Project management plan",
                                         "Project documents (lessons learned register, stakeholder register, team assignments)",
                                         "Deliverables",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Knowledge management (information management, knowledge sharing)",
                                                   "Information management (workarounds, library services, lessons learned)",
                                                   "Interpersonal and team skills (active listening, facilitation, leadership, networking, political awareness)"
                                               ],
                          "outputs":  [
                                          "Lessons learned register",
                                          "Project management plan updates",
                                          "Organizational process assets updates"
                                      ],
                          "exam_traps":  [
                                             "Tacit knowledge (in people\u0027s heads) is harder to share than explicit knowledge (documented)",
                                             "Knowledge management is about BOTH using existing knowledge AND creating new knowledge",
                                             "Lessons learned should be captured throughout the project, not just at the end"
                                         ],
                          "agile_considerations":  [
                                                       "Retrospectives are a key tool for knowledge management in agile",
                                                       "Pair programming and swarming share tacit knowledge"
                                                   ]
                      },
                      {
                          "id":  "4.5",
                          "name":  "Monitor and Control Project Work",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of tracking, reviewing, and reporting the overall progress to meet the performance objectives defined in the project management plan.",
                          "inputs":  [
                                         "Project management plan",
                                         "Project documents (assumption log, basis of estimates, cost forecasts, etc.)",
                                         "Work performance information",
                                         "Agreements",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data analysis (alternatives analysis, cost-benefit analysis, earned value analysis, root cause analysis, trend analysis, variance analysis)",
                                                   "Decision making (voting)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Work performance reports",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Work performance INFORMATION is input, work performance REPORTS are output",
                                             "Variance analysis compares actual to planned — this is key for EVM questions",
                                             "Trend analysis helps predict future performance based on past results"
                                         ],
                          "agile_considerations":  [
                                                       "Burndown/burnup charts track progress in agile",
                                                       "Cumulative flow diagrams help identify bottlenecks"
                                                   ]
                      },
                      {
                          "id":  "4.6",
                          "name":  "Perform Integrated Change Control",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of reviewing all change requests; approving changes and managing changes to deliverables, project documents, and the project management plan; and communicating the decisions.",
                          "inputs":  [
                                         "Project management plan (change management plan, configuration management plan, scope baseline, etc.)",
                                         "Project documents (basis of estimates, requirements traceability matrix, risk report)",
                                         "Work performance reports",
                                         "Change requests",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Change control tools",
                                                   "Data analysis (alternatives analysis, cost-benefit analysis)",
                                                   "Decision making (voting, autocratic decision making, multicriteria decision analysis)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Approved change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "ANY change to baselines must go through ICC — no exceptions",
                                             "The CCB (Change Control Board) approves or rejects changes — the PM facilitates",
                                             "Emergency changes may be approved in absentia but MUST be reviewed later",
                                             "Configuration management ensures version control of deliverables and documents"
                                         ],
                          "agile_considerations":  [
                                                       "In agile, change is expected — but still needs to be communicated and tracked",
                                                       "Product owner prioritizes changes to the backlog"
                                                   ]
                      },
                      {
                          "id":  "4.7",
                          "name":  "Close Project or Phase",
                          "process_group":  "Closing",
                          "description":  "The process of finalizing all activities for the project, phase, or contract.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan",
                                         "Project documents (assumption log, basis of estimates, change log, issue log, etc.)",
                                         "Accepted deliverables",
                                         "Business documents (business case, benefits management plan)",
                                         "Agreements",
                                         "Procurement documentation",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data analysis (document analysis, regression analysis, trend analysis, variance analysis)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Project documents updates",
                                          "Final product, service, or result transition",
                                          "Final report",
                                          "Organizational process assets updates"
                                      ],
                          "exam_traps":  [
                                             "Administrative closure happens even if project is terminated early",
                                             "Final report summarizes overall success and documents lessons learned",
                                             "OPAs are updated with lessons learned, project files, and closure documents",
                                             "Celebrate success — even for failed projects, recognize the team"
                                         ],
                          "agile_considerations":  [
                                                       "Release retrospectives capture lessons learned at the end of each release",
                                                       "Agile projects may not have a formal \u0027close\u0027 until the product is retired"
                                                   ]
                      }
                  ],
    "key_formulas":  [
                         {
                             "name":  "Earned Value Management",
                             "formulas":  [
                                              "PV (Planned Value) = Budgeted cost of work scheduled",
                                              "EV (Earned Value) = Budgeted cost of work performed",
                                              "AC (Actual Cost) = Actual cost of work performed",
                                              "SV (Schedule Variance) = EV - PV",
                                              "CV (Cost Variance) = EV - AC",
                                              "SPI (Schedule Performance Index) = EV / PV",
                                              "CPI (Cost Performance Index) = EV / AC",
                                              "EAC (Estimate at Completion) = BAC / CPI (if current trends continue)",
                                              "ETC (Estimate to Complete) = EAC - AC",
                                              "VAC (Variance at Completion) = BAC - EAC",
                                              "TCPI (To-Complete Performance Index) = (BAC - EV) / (BAC - AC)"
                                          ]
                         }
                     ],
    "exam_tips":  [
                      "Integration is where ALL knowledge areas come together — expect cross-domain questions",
                      "The PM plan is the central document — know what\u0027s in it vs. what\u0027s in subsidiary plans",
                      "Change control is heavily tested — know the ICC process inside out",
                      "Understand the data flow: Work performance DATA → INFORMATION → REPORTS",
                      "Know when the PM can decide vs. when the CCB/sponsor must approve",
                      "Lessons learned are updated throughout — not just at the end"
                  ]
}

STUDY_GUIDES['scope-management'] = {
    "id":  "scope-management",
    "name":  "Project Scope Management",
    "description":  "Includes the processes required to ensure the project includes all the work required, and only the work required, to complete the project successfully.",
    "processes":  [
                      {
                          "id":  "5.1",
                          "name":  "Plan Scope Management",
                          "process_group":  "Planning",
                          "description":  "The process of creating a scope management plan that documents how the project and product scope will be defined, validated, and controlled.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan (quality management plan, project life cycle description, development approach)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data analysis (alternatives analysis)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Scope management plan",
                                          "Requirements management plan"
                                      ],
                          "exam_traps":  [
                                             "The scope management plan describes HOW to manage scope — not the actual scope",
                                             "The requirements management plan describes HOW to collect, analyze, and document requirements",
                                             "Both are part of the project management plan"
                                         ],
                          "agile_considerations":  [
                                                       "In agile, scope is managed through the product backlog and iteration planning",
                                                       "Scope may evolve — the scope management plan defines how changes are handled"
                                                   ]
                      },
                      {
                          "id":  "5.2",
                          "name":  "Collect Requirements",
                          "process_group":  "Planning",
                          "description":  "The process of determining, documenting, and managing stakeholder needs and requirements to meet project objectives.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan (scope management plan, requirements management plan, stakeholder engagement plan)",
                                         "Project documents (assumption log, lessons learned register, stakeholder register)",
                                         "Business documents (business case)",
                                         "Agreements",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (brainstorming, interviews, focus groups, questionnaires, surveys, benchmarking)",
                                                   "Data analysis (document analysis)",
                                                   "Decision making (voting, multicriteria decision analysis)",
                                                   "Data representation (affinity diagrams, mind mapping)",
                                                   "Interpersonal and team skills (nominal group technique, observation/conversation, facilitation)",
                                                   "Context diagram",
                                                   "Prototypes"
                                               ],
                          "outputs":  [
                                          "Requirements documentation",
                                          "Requirements traceability matrix (RTM)"
                                      ],
                          "exam_traps":  [
                                             "The RTM links requirements to their origin, tracks them through the project, and verifies delivery",
                                             "Requirements must be measurable, testable, and traceable",
                                             "Unstated requirements are a major source of scope creep — always document them",
                                             "Prototypes help stakeholders visualize the end product before it\u0027s built"
                                         ],
                          "agile_considerations":  [
                                                       "User stories are the primary requirements format in agile",
                                                       "Definition of Ready (DoR) ensures requirements are clear before work starts",
                                                       "Product owner is responsible for requirements prioritization"
                                                   ]
                      },
                      {
                          "id":  "5.3",
                          "name":  "Define Scope",
                          "process_group":  "Planning",
                          "description":  "The process of developing a detailed description of the project and product.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan (scope management plan)",
                                         "Project documents (assumption log, requirements documentation, risk register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data analysis (alternatives analysis, document analysis)",
                                                   "Decision making (multicriteria decision analysis)",
                                                   "Interpersonal and team skills (facilitation)",
                                                   "Product analysis"
                                               ],
                          "outputs":  [
                                          "Project scope statement",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "The project scope statement includes: product scope description, acceptance criteria, deliverables, exclusions, constraints, and assumptions",
                                             "Exclusions are just as important as inclusions — they prevent scope creep",
                                             "The scope statement is the basis for the WBS and project baseline",
                                             "Product scope = features and functions; Project scope = work to deliver the product"
                                         ],
                          "agile_considerations":  [
                                                       "In agile, scope is defined through the product vision, roadmap, and backlog",
                                                       "Scope may be refined iteratively — but the vision remains stable"
                                                   ]
                      },
                      {
                          "id":  "5.4",
                          "name":  "Create WBS",
                          "process_group":  "Planning",
                          "description":  "The process of subdividing project deliverables and project work into smaller, more manageable components.",
                          "inputs":  [
                                         "Project management plan (scope management plan)",
                                         "Project documents (project scope statement, requirements documentation)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Decomposition",
                                                   "Rolling wave planning"
                                               ],
                          "outputs":  [
                                          "Scope baseline (project scope statement + WBS + WBS dictionary)",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "The WBS is a hierarchical decomposition of the total scope of work — 100% rule applies",
                                             "Work packages are the lowest level of the WBS — they\u0027re what get scheduled and budgeted",
                                             "The WBS dictionary describes each WBS element in detail",
                                             "Scope baseline = scope statement + WBS + WBS dictionary",
                                             "The WBS should NOT include activities — those come later in Define Activities"
                                         ],
                          "agile_considerations":  [
                                                       "In agile, the backlog is a flat WBS equivalent",
                                                       "Epics → Features → User Stories → Tasks is a common agile hierarchy",
                                                       "Rolling wave planning is natural in agile"
                                                   ]
                      },
                      {
                          "id":  "5.5",
                          "name":  "Validate Scope",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of formalizing acceptance of the completed project deliverables.",
                          "inputs":  [
                                         "Project management plan (scope management plan, requirements management plan, scope baseline)",
                                         "Project documents (lessons learned register, quality reports, requirements documentation, requirements traceability matrix)",
                                         "Verified deliverables",
                                         "Work performance data"
                                     ],
                          "tools_techniques":  [
                                                   "Inspection",
                                                   "Decision making (voting)"
                                               ],
                          "outputs":  [
                                          "Accepted deliverables",
                                          "Work performance information",
                                          "Change requests",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Validate Scope = formal acceptance by the customer/sponsor (external acceptance)",
                                             "Control Quality = checking deliverables are correct (internal verification)",
                                             "Validate Scope happens AFTER Control Quality — inspect internally first, then get external sign-off",
                                             "If deliverables are rejected, create change requests for defect repair"
                                         ],
                          "agile_considerations":  [
                                                       "In agile, scope validation happens at the end of each iteration/sprint review",
                                                       "Product owner accepts user stories during sprint review",
                                                       "Working software is the primary measure of progress"
                                                   ]
                      },
                      {
                          "id":  "5.6",
                          "name":  "Control Scope",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of monitoring the status of the project and product scope and managing changes to the scope baseline.",
                          "inputs":  [
                                         "Project management plan (scope management plan, requirements management plan, change management plan, configuration management plan, scope baseline, performance measurement baseline)",
                                         "Project documents (lessons learned register, requirements documentation, requirements traceability matrix)",
                                         "Work performance data",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Data analysis (variance analysis, trend analysis)"
                                               ],
                          "outputs":  [
                                          "Work performance information",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Scope creep = uncontrolled expansion of scope — PREVENT it with strict change control",
                                             "Gold plating = adding extra features not in scope — it\u0027s BAD, even with good intentions",
                                             "Use variance analysis to compare actual scope to the scope baseline",
                                             "The scope baseline should only change through formal change control"
                                         ],
                          "agile_considerations":  [
                                                       "In agile, scope changes are expected and managed through the backlog",
                                                       "Product owner reprioritizes backlog items when scope changes",
                                                       "Timeboxed iterations limit scope creep — only change what\u0027s in the next iteration"
                                                   ]
                      }
                  ],
    "key_formulas":  [

                     ],
    "exam_tips":  [
                      "Know the difference between Validate Scope (external acceptance) and Control Quality (internal verification)",
                      "Scope baseline = scope statement + WBS + WBS dictionary — this is CRITICAL",
                      "The 100% rule: every level of decomposition must represent 100% of the parent",
                      "Gold plating is always wrong — it creates risk and wastes resources",
                      "Scope creep is uncontrolled — change control is how you manage it properly",
                      "Requirements traceability matrix links requirements to deliverables, tests, and acceptance criteria"
                  ]
}

STUDY_GUIDES['schedule-management'] = {
    "id":  "schedule-management",
    "name":  "Project Schedule Management",
    "description":  "Includes the processes required to manage the timely completion of the project.",
    "processes":  [
                      {
                          "id":  "6.1",
                          "name":  "Plan Schedule Management",
                          "process_group":  "Planning",
                          "description":  "The process of establishing the policies, procedures, and documentation for planning, developing, managing, executing, and controlling the project schedule.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan (scope management plan, development approach)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data analysis (alternatives analysis)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Schedule management plan"
                                      ],
                          "exam_traps":  [
                                             "The schedule management plan is a COMPONENT of the project management plan, not a separate document",
                                             "It defines how the schedule will be managed, not the actual schedule",
                                             "Includes criteria for scheduling tools, level of accuracy, and control thresholds"
                                         ],
                          "agile_considerations":  [
                                                       "In agile, the schedule management plan may define iteration length and release planning",
                                                       "Rolling wave planning is common for adaptive approaches"
                                                   ]
                      },
                      {
                          "id":  "6.2",
                          "name":  "Define Activities",
                          "process_group":  "Planning",
                          "description":  "The process of identifying and documenting the specific actions to be performed to produce the project deliverables.",
                          "inputs":  [
                                         "Project management plan (schedule management plan, scope baseline)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Decomposition",
                                                   "Rolling wave planning",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Activity list",
                                          "Activity attributes",
                                          "Milestone list",
                                          "Change requests",
                                          "Project management plan updates"
                                      ],
                          "exam_traps":  [
                                             "Activities are the LOWEST level of the WBS — work packages get decomposed into activities",
                                             "Milestones have ZERO duration — they mark significant events",
                                             "Rolling wave planning is used when future work cannot be detailed"
                                         ],
                          "agile_considerations":  [
                                                       "In agile, activities are derived from user stories in the sprint backlog",
                                                       "Activities may be defined just-in-time before iteration planning"
                                                   ]
                      },
                      {
                          "id":  "6.3",
                          "name":  "Sequence Activities",
                          "process_group":  "Planning",
                          "description":  "The process of identifying and documenting relationships among the project activities.",
                          "inputs":  [
                                         "Project management plan (schedule management plan, scope baseline)",
                                         "Project documents (activity list, activity attributes, milestone list, assumption log)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Precedence diagramming method (PDM)",
                                                   "Dependency determination and integration",
                                                   "Leads and lags"
                                               ],
                          "outputs":  [
                                          "Project schedule network diagrams",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "FS (Finish-to-Start) is the MOST COMMON dependency type",
                                             "SF (Start-to-Finish) is the LEAST COMMON and rarely used",
                                             "Leads accelerate successor activities (negative lag)",
                                             "Lags delay successor activities (positive lag)",
                                             "Mandatory dependencies are inherent in the nature of work (hard logic)"
                                         ],
                          "agile_considerations":  [
                                                       "Dependencies are managed through sprint planning and daily stand-ups",
                                                       "Self-organizing teams identify and resolve dependencies collaboratively"
                                                   ]
                      },
                      {
                          "id":  "6.4",
                          "name":  "Estimate Activity Durations",
                          "process_group":  "Planning",
                          "description":  "The process of estimating the number of work periods needed to complete individual activities with estimated resources.",
                          "inputs":  [
                                         "Project management plan (schedule management plan, scope baseline)",
                                         "Project documents (activity list, activity attributes, milestone list, resource requirements, resource breakdown structure, resource calendars, risk register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Analogous estimating",
                                                   "Parametric estimating",
                                                   "Three-point estimating",
                                                   "Bottom-up estimating",
                                                   "Data analysis (alternatives analysis, reserve analysis)",
                                                   "Decision making (voting)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Duration estimates",
                                          "Basis of estimates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Analogous estimating is LESS accurate but FASTER — uses historical data from similar projects",
                                             "Parametric estimating uses a statistical relationship between historical data and variables",
                                             "Three-point estimating uses optimistic, pessimistic, and most likely (PERT = (O + 4M + P) / 6)",
                                             "Bottom-up estimating is MOST accurate but MOST time-consuming",
                                             "Reserve analysis adds contingency reserves for identified risks"
                                         ],
                          "agile_considerations":  [
                                                       "Story points are used instead of time-based estimates",
                                                       "Velocity helps predict how many story points a team can complete per iteration"
                                                   ]
                      },
                      {
                          "id":  "6.5",
                          "name":  "Develop Schedule",
                          "process_group":  "Planning",
                          "description":  "The process of analyzing activity sequences, durations, resource requirements, and schedule constraints to create the project schedule model.",
                          "inputs":  [
                                         "Project management plan (schedule management plan, scope baseline)",
                                         "Project documents (activity list, activity attributes, project schedule network diagrams, activity duration estimates, duration estimates, resource requirements, resource calendars)",
                                         "Agreements",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Schedule network analysis",
                                                   "Critical path method",
                                                   "Resource optimization",
                                                   "Data analysis (what-if scenario analysis, simulation)",
                                                   "Leads and lags",
                                                   "Schedule compression",
                                                   "Project management information system (PMIS)",
                                                   "Agile release planning"
                                               ],
                          "outputs":  [
                                          "Schedule baseline",
                                          "Project schedule",
                                          "Schedule data",
                                          "Project calendars",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Critical Path = the LONGEST path through the network — determines shortest project duration",
                                             "Total Float (Slack) = amount of time an activity can be delayed without delaying the project",
                                             "Free Float = amount of time an activity can be delayed without delaying the EARLY START of successor",
                                             "Fast tracking = doing activities in parallel that are normally sequential (INCREASES risk)",
                                             "Crashing = adding resources to shorten duration (INCREASES cost)",
                                             "Resource leveling can extend the project duration but optimizes resource usage"
                                         ],
                          "agile_considerations":  [
                                                       "Release planning defines when features will be delivered",
                                                       "Sprint/iteration planning is done at the start of each iteration",
                                                       "Burndown charts track remaining work against time"
                                                   ]
                      },
                      {
                          "id":  "6.6",
                          "name":  "Control Schedule",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of monitoring the status of project activities to update project progress and manage changes to the schedule baseline.",
                          "inputs":  [
                                         "Project management plan (schedule management plan, schedule baseline, scope baseline, performance measurement baseline)",
                                         "Project documents (project schedule, project calendars, schedule data, resource calendars)",
                                         "Work performance data",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Data analysis (earned value analysis, iteration burndown chart, performance reviews, trend analysis, variance analysis, what-if scenario analysis)",
                                                   "Critical path method",
                                                   "Project management information system (PMIS)",
                                                   "Resource optimization",
                                                   "Leads and lags",
                                                   "Schedule compression"
                                               ],
                          "outputs":  [
                                          "Work performance information",
                                          "Schedule forecasts",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "EVM metrics for schedule: SV = EV - PV, SPI = EV / PV",
                                             "SPI \u003c 1.0 means behind schedule, SPI \u003e 1.0 means ahead of schedule",
                                             "Trend analysis predicts future performance based on past results",
                                             "Schedule compression is used when the project is behind schedule"
                                         ],
                          "agile_considerations":  [
                                                       "Burndown/burnup charts are primary schedule tracking tools",
                                                       "Velocity trends help predict future iteration capacity",
                                                       "Cumulative flow diagrams show work-in-progress and bottlenecks"
                                                   ]
                      }
                  ],
    "key_formulas":  [
                         {
                             "name":  "Critical Path Method (CPM)",
                             "formulas":  [
                                              "Early Start (ES) = Maximum EF of all predecessors",
                                              "Early Finish (EF) = ES + Duration",
                                              "Late Finish (LF) = Minimum LS of all successors",
                                              "Late Start (LS) = LF - Duration",
                                              "Total Float = LS - ES or LF - EF",
                                              "Free Float = ES of successor - EF of current activity"
                                          ]
                         },
                         {
                             "name":  "PERT Three-Point Estimating",
                             "formulas":  [
                                              "Expected Duration = (Optimistic + 4×Most Likely + Pessimistic) / 6",
                                              "Standard Deviation = (Pessimistic - Optimistic) / 6",
                                              "Variance = [(Pessimistic - Optimistic) / 6]²"
                                          ]
                         }
                     ],
    "exam_tips":  [
                      "Know the difference between FS, SS, FF, SF dependencies — FS is most common, SF is rare",
                      "Critical path has ZERO float — any delay delays the project",
                      "Fast tracking increases risk; crashing increases cost",
                      "Resource leveling may extend the schedule but smooths resource demand",
                      "Float calculations are heavily tested — practice forward and backward passes",
                      "Agile uses story points and velocity, not time-based estimates",
                      "Always consider the project\u0027s critical path when evaluating schedule changes"
                  ]
}

STUDY_GUIDES['cost-management'] = {
    "id":  "cost-management",
    "name":  "Project Cost Management",
    "description":  "Includes the processes involved in planning, estimating, budgeting, financing, funding, managing, and controlling costs so the project can be completed within the approved budget.",
    "processes":  [
                      {
                          "id":  "7.1",
                          "name":  "Plan Cost Management",
                          "process_group":  "Planning",
                          "description":  "The process of defining how the project costs will be estimated, budgeted, managed, monitored, and controlled.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan (schedule management plan, risk management plan)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data analysis (alternatives analysis)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Cost management plan"
                                      ],
                          "exam_traps":  [
                                             "The cost management plan establishes how costs will be managed, not the actual budget",
                                             "Includes units of measure, level of precision, control thresholds, and reporting formats",
                                             "Links to other plans like scope, schedule, and risk management"
                                         ],
                          "agile_considerations":  [
                                                       "Cost management may focus on team capacity and iteration costs",
                                                       "Value-based delivery prioritizes high-value features first"
                                                   ]
                      },
                      {
                          "id":  "7.2",
                          "name":  "Estimate Costs",
                          "process_group":  "Planning",
                          "description":  "The process of developing an approximation of the monetary resources needed to complete project work.",
                          "inputs":  [
                                         "Project management plan (cost management plan, quality management plan, scope baseline)",
                                         "Project documents (lessons learned register, project schedule, resource requirements, risk register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Analogous estimating",
                                                   "Parametric estimating",
                                                   "Bottom-up estimating",
                                                   "Three-point estimating",
                                                   "Data analysis (alternatives analysis, reserve analysis, cost of quality)",
                                                   "Project management information system (PMIS)",
                                                   "Decision making (voting)"
                                               ],
                          "outputs":  [
                                          "Cost estimates",
                                          "Basis of estimates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Cost estimates should include all resources (labor, materials, equipment, services, facilities)",
                                             "Indirect costs (overhead) must be included in estimates",
                                             "Contingency reserves are for KNOWN risks (included in cost baseline)",
                                             "Management reserves are for UNKNOWN risks (included in project budget, NOT baseline)"
                                         ],
                          "agile_considerations":  [
                                                       "Cost estimates may be based on team velocity and iteration costs",
                                                       "Rolling wave planning allows for progressive elaboration of costs"
                                                   ]
                      },
                      {
                          "id":  "7.3",
                          "name":  "Determine Budget",
                          "process_group":  "Planning",
                          "description":  "The process of aggregating the estimated costs of individual activities or work packages to establish an authorized cost baseline.",
                          "inputs":  [
                                         "Project management plan (cost management plan, resource management plan, scope baseline)",
                                         "Project documents (basis of estimates, cost estimates, project schedule, risk register)",
                                         "Business documents (business case, benefits management plan)",
                                         "Agreements",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Cost aggregation",
                                                   "Data analysis (reserve analysis)",
                                                   "Historical information review",
                                                   "Funding limit reconciliation",
                                                   "Financing"
                                               ],
                          "outputs":  [
                                          "Cost baseline",
                                          "Project funding requirements",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Cost baseline = sum of all work package estimates + contingency reserves",
                                             "Project budget = cost baseline + management reserve",
                                             "Funding requirements are often expressed as S-curves (incremental funding)",
                                             "Cost baseline is a TIME-PHASED budget — it shows when money will be spent",
                                             "Management reserve requires approval to use; contingency reserve is part of baseline"
                                         ],
                          "agile_considerations":  [
                                                       "Budget may be allocated per release or iteration",
                                                       "Value-based prioritization ensures highest ROI features are delivered first"
                                                   ]
                      },
                      {
                          "id":  "7.4",
                          "name":  "Control Costs",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of monitoring the status of the project to update the project costs and managing changes to the cost baseline.",
                          "inputs":  [
                                         "Project management plan (cost management plan, cost baseline, performance measurement baseline)",
                                         "Project documents (lessons learned register)",
                                         "Project funding requirements",
                                         "Work performance data",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data analysis (earned value analysis, variance analysis, trend analysis, reserve analysis)",
                                                   "To-complete performance index (TCPI)",
                                                   "Project management information system (PMIS)"
                                               ],
                          "outputs":  [
                                          "Work performance information",
                                          "Cost forecasts",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "EVM is the PRIMARY tool for cost control — know ALL formulas!",
                                             "CPI \u003c 1.0 = over budget, CPI \u003e 1.0 = under budget",
                                             "CV = EV - AC (negative = over budget, positive = under budget)",
                                             "EAC = BAC / CPI (if current trends continue)",
                                             "TCPI \u003e 1.0 = must work harder (more efficiently) to meet budget"
                                         ],
                          "agile_considerations":  [
                                                       "Burn rate tracking monitors cost per iteration",
                                                       "Velocity helps predict if budget will be sufficient for planned scope"
                                                   ]
                      }
                  ],
    "key_formulas":  [
                         {
                             "name":  "Earned Value Management (EVM)",
                             "formulas":  [
                                              "PV (Planned Value) = Budgeted cost of work scheduled",
                                              "EV (Earned Value) = Budgeted cost of work performed",
                                              "AC (Actual Cost) = Actual cost of work performed",
                                              "SV (Schedule Variance) = EV - PV",
                                              "CV (Cost Variance) = EV - AC",
                                              "SPI (Schedule Performance Index) = EV / PV",
                                              "CPI (Cost Performance Index) = EV / AC",
                                              "EAC (Estimate at Completion) = BAC / CPI",
                                              "ETC (Estimate to Complete) = EAC - AC",
                                              "VAC (Variance at Completion) = BAC - EAC",
                                              "TCPI (To-Complete Performance Index) = (BAC - EV) / (BAC - AC)"
                                          ]
                         },
                         {
                             "name":  "Reserve Calculations",
                             "formulas":  [
                                              "Cost Baseline = Sum of work package estimates + Contingency Reserve",
                                              "Project Budget = Cost Baseline + Management Reserve",
                                              "Contingency Reserve = for known risks (part of baseline)",
                                              "Management Reserve = for unknown risks (requires approval)"
                                          ]
                         }
                     ],
    "exam_tips":  [
                      "MEMORIZE all EVM formulas — they are heavily tested!",
                      "CPI and SPI: \u003e1.0 is good, \u003c1.0 is bad",
                      "CV and SV: positive is good, negative is bad",
                      "TCPI: \u003e1.0 means must improve efficiency; \u003c1.0 means can be less efficient",
                      "Contingency reserve is for KNOWN unknowns; management reserve is for UNKNOWN unknowns",
                      "Cost baseline is time-phased; project budget includes management reserve",
                      "Always use EVM to forecast final costs (EAC) and remaining work (ETC)"
                  ]
}

STUDY_GUIDES['quality-management'] = {
    "id":  "quality-management",
    "name":  "Project Quality Management",
    "description":  "Includes the processes for incorporating the organization\u0027s quality policy regarding planning, managing, and controlling project and product quality requirements.",
    "processes":  [
                      {
                          "id":  "8.1",
                          "name":  "Plan Quality Management",
                          "process_group":  "Planning",
                          "description":  "The process of identifying quality requirements and/or standards for the project and its deliverables, and documenting how the project will demonstrate compliance.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan (scope baseline, schedule baseline, cost baseline, risk management plan, stakeholder engagement plan)",
                                         "Project documents (assumption log, requirements documentation, requirements traceability matrix, risk register, stakeholder register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (benchmarking, brainstorming, interviews)",
                                                   "Data analysis (cost-benefit analysis, cost of quality)",
                                                   "Decision making (multicriteria decision analysis)",
                                                   "Data representation (flowcharts, logical data model, matrix diagrams, mind mapping)",
                                                   "Test and inspection planning"
                                               ],
                          "outputs":  [
                                          "Quality management plan",
                                          "Quality metrics",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Quality management plan is part of the project management plan",
                                             "Cost of Quality (COQ) includes prevention costs, appraisal costs, and failure costs (internal + external)",
                                             "Prevention is cheaper than inspection; inspection is cheaper than failure",
                                             "Quality should be planned in, not inspected in"
                                         ],
                          "agile_considerations":  [
                                                       "Definition of Done (DoD) defines quality standards for each increment",
                                                       "Continuous integration and automated testing ensure quality throughout",
                                                       "Pair programming and code reviews improve quality"
                                                   ]
                      },
                      {
                          "id":  "8.2",
                          "name":  "Manage Quality",
                          "process_group":  "Executing",
                          "description":  "The process of translating the quality management plan into executable quality activities that incorporate the organization\u0027s quality policies into the project.",
                          "inputs":  [
                                         "Project management plan (quality management plan)",
                                         "Project documents (lessons learned register, quality control measurements, quality metrics, risk report)",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Data gathering (checklists)",
                                                   "Data analysis (alternatives analysis, document analysis, process analysis, root cause analysis)",
                                                   "Decision making (multicriteria decision analysis)",
                                                   "Data representation (affinity diagrams, cause-and-effect diagrams, flowcharts, histograms, matrix diagrams, scatter diagrams)",
                                                   "Audits",
                                                   "Design for X",
                                                   "Problem solving",
                                                   "Quality improvement methods"
                                               ],
                          "outputs":  [
                                          "Quality reports",
                                          "Test and evaluation documents",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Manage Quality = Quality Assurance (QA) — focuses on PROCESSES",
                                             "Audits are structured reviews to ensure compliance with policies",
                                             "Root cause analysis finds the underlying reason for defects",
                                             "Cause-and-effect diagrams (fishbone/Ishikawa) help identify root causes",
                                             "Manage Quality is PROACTIVE; Control Quality is REACTIVE"
                                         ],
                          "agile_considerations":  [
                                                       "Frequent retrospectives identify process improvements",
                                                       "Continuous integration catches defects early",
                                                       "Collective code ownership improves quality"
                                                   ]
                      },
                      {
                          "id":  "8.3",
                          "name":  "Control Quality",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of monitoring and recording results of executing quality management activities to assess performance and ensure project outputs are complete, correct, and meet customer expectations.",
                          "inputs":  [
                                         "Project management plan (quality management plan)",
                                         "Project documents (lessons learned register, quality metrics, test and evaluation documents)",
                                         "Approved deliverables",
                                         "Work performance data",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Data gathering (checklists, check sheets, statistical sampling, questionnaires, surveys)",
                                                   "Data analysis (performance reviews, root cause analysis)",
                                                   "Inspection",
                                                   "Testing/product evaluations"
                                               ],
                          "outputs":  [
                                          "Quality control measurements",
                                          "Verified deliverables",
                                          "Work performance information",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Control Quality focuses on SPECIFIC DELIVERABLES (inspect the product)",
                                             "Manage Quality focuses on PROCESSES (improve how we work)",
                                             "Inspection can happen at any level (single activity to final product)",
                                             "Control Quality produces verified deliverables that go to Validate Scope",
                                             "Statistical sampling reduces inspection costs while maintaining confidence"
                                         ],
                          "agile_considerations":  [
                                                       "Automated testing provides rapid feedback on quality",
                                                       "Definition of Done ensures consistent quality criteria",
                                                       "Sprint reviews validate that increments meet quality standards"
                                                   ]
                      }
                  ],
    "key_formulas":  [

                     ],
    "exam_tips":  [
                      "Plan Quality = set standards and criteria",
                      "Manage Quality = ensure processes will produce quality (QA)",
                      "Control Quality = inspect specific deliverables (QC)",
                      "Cost of Quality: Prevention \u003c Appraisal \u003c Internal Failure \u003c External Failure",
                      "Seven Basic Quality Tools: Cause-and-effect, Flowchart, Checksheet, Pareto, Histogram, Control chart, Scatter diagram",
                      "Control limits (3 sigma) are process-driven; Specification limits are customer-driven",
                      "Rule of Seven: seven consecutive points on one side of mean = process out of control"
                  ]
}

STUDY_GUIDES['resource-management'] = {
    "id":  "resource-management",
    "name":  "Project Resource Management",
    "description":  "Includes the processes to identify, acquire, and manage the resources needed for the successful completion of the project.",
    "processes":  [
                      {
                          "id":  "9.1",
                          "name":  "Plan Resource Management",
                          "process_group":  "Planning",
                          "description":  "The process of defining how to estimate, acquire, manage, and use physical and team resources.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan (quality management plan, scope baseline)",
                                         "Project documents (project schedule, requirements documentation, risk register, stakeholder register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data representation (hierarchical charts, responsibility assignment matrix, text-oriented formats)",
                                                   "Organizational theory",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Resource management plan",
                                          "Team charter",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "RACI matrix shows WHO does WHAT: R=Responsible, A=Accountable, C=Consulted, I=Informed",
                                             "Only ONE person can be Accountable (A) for each task",
                                             "Resource management plan covers both TEAM resources and PHYSICAL resources",
                                             "Team charter establishes team operating guidelines and values"
                                         ],
                          "agile_considerations":  [
                                                       "Self-organizing teams reduce need for detailed resource assignment matrices",
                                                       "Team charter supports agile values and working agreements"
                                                   ]
                      },
                      {
                          "id":  "9.2",
                          "name":  "Estimate Activity Resources",
                          "process_group":  "Planning",
                          "description":  "The process of estimating team resources and the type and quantities of materials, equipment, and supplies necessary to perform project work.",
                          "inputs":  [
                                         "Project management plan (resource management plan, scope baseline)",
                                         "Project documents (activity attributes, activity list, assumption log, cost estimates, resource calendars, risk register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Bottom-up estimating",
                                                   "Analogous estimating",
                                                   "Parametric estimating",
                                                   "Data analysis (alternatives analysis)",
                                                   "Project management information system (PMIS)"
                                               ],
                          "outputs":  [
                                          "Resource requirements",
                                          "Basis of estimates",
                                          "Resource breakdown structure",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Resource requirements identify TYPE and QUANTITY of resources needed",
                                             "Resource Breakdown Structure (RBS) is hierarchical, similar to WBS but for resources",
                                             "Consider both team members (human resources) and physical resources (equipment, materials)"
                                         ],
                          "agile_considerations":  [
                                                       "Team capacity is estimated based on velocity and team size",
                                                       "Generalizing specialists (T-shaped skills) improve team flexibility"
                                                   ]
                      },
                      {
                          "id":  "9.3",
                          "name":  "Acquire Resources",
                          "process_group":  "Executing",
                          "description":  "The process of obtaining team members, facilities, equipment, materials, supplies, and other resources necessary to complete project work.",
                          "inputs":  [
                                         "Project management plan (resource management plan, procurement management plan, cost baseline)",
                                         "Project documents (project schedule, resource calendars, resource requirements, stakeholder register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Decision making (multicriteria decision analysis)",
                                                   "Interpersonal and team skills (negotiation, influencing)",
                                                   "Pre-assignment",
                                                   "Virtual teams"
                                               ],
                          "outputs":  [
                                          "Physical resource assignments",
                                          "Team assignments",
                                          "Resource calendars",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates",
                                          "Enterprise environmental factors updates",
                                          "Organizational process assets updates"
                                      ],
                          "exam_traps":  [
                                             "Pre-assignment occurs when resources are named in the charter or contract",
                                             "Negotiation is needed when resources are shared across projects or departments",
                                             "Virtual teams require more communication planning",
                                             "Resource calendars show WHEN resources are available"
                                         ],
                          "agile_considerations":  [
                                                       "Co-located teams are preferred but virtual teams are common",
                                                       "Self-organizing teams select their own members when possible"
                                                   ]
                      },
                      {
                          "id":  "9.4",
                          "name":  "Develop Team",
                          "process_group":  "Executing",
                          "description":  "The process of improving competencies, team member interaction, and the overall team environment to enhance project performance.",
                          "inputs":  [
                                         "Project management plan (resource management plan)",
                                         "Project documents (lessons learned register, project schedule, resource calendars, resource requirements, team assignments)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Colocation",
                                                   "Virtual teams",
                                                   "Communication technology",
                                                   "Interpersonal and team skills (conflict management, influencing, motivation, negotiation, team building)",
                                                   "Recognition and rewards",
                                                   "Training",
                                                   "Individual and team assessments",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Team performance assessments",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates",
                                          "Enterprise environmental factors updates",
                                          "Organizational process assets updates"
                                      ],
                          "exam_traps":  [
                                             "Develop Team focuses on improving TEAM PERFORMANCE (skills + interactions)",
                                             "Tuckman\u0027s stages: Forming → Storming → Norming → Performing → Adjourning",
                                             "Team performance assessments evaluate effectiveness, not individual performance",
                                             "Recognition and rewards should consider cultural differences",
                                             "Training is a cost to the project, not a benefit"
                                         ],
                          "agile_considerations":  [
                                                       "Servant leadership empowers teams to self-organize",
                                                       "Retrospectives are key for continuous team improvement",
                                                       "Team building happens continuously, not just at project start"
                                                   ]
                      },
                      {
                          "id":  "9.5",
                          "name":  "Manage Team",
                          "process_group":  "Executing",
                          "description":  "The process of tracking team member performance, providing feedback, resolving issues, and managing team changes to optimize project performance.",
                          "inputs":  [
                                         "Project management plan (resource management plan)",
                                         "Project documents (issue log, lessons learned register, project team assignments, team charter)",
                                         "Work performance reports",
                                         "Team performance assessments",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Interpersonal and team skills (conflict management, decision making, emotional intelligence, influencing, leadership)",
                                                   "Project management information system (PMIS)"
                                               ],
                          "outputs":  [
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates",
                                          "Enterprise environmental factors updates"
                                      ],
                          "exam_traps":  [
                                             "Manage Team focuses on DAY-TO-DAY management of team members",
                                             "Conflict resolution methods: Withdraw/Avoid, Smooth/Accommodate, Compromise/Reconcile, Force/Direct, Collaborate/Problem Solve, Confront/Problem Solve",
                                             "Collaborating/Problem Solving is the PREFERRED method (win-win)",
                                             "Forcing/Directing is a win-lose approach — use only in emergencies",
                                             "Emotional intelligence is critical for managing teams effectively"
                                         ],
                          "agile_considerations":  [
                                                       "Self-organizing teams reduce the need for direct management",
                                                       "Servant leadership supports team autonomy while removing impediments"
                                                   ]
                      },
                      {
                          "id":  "9.6",
                          "name":  "Control Resources",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of ensuring that the physical resources assigned and allocated to the project are available as planned, as well as monitoring the planned versus actual use of resources.",
                          "inputs":  [
                                         "Project management plan (resource management plan)",
                                         "Project documents (issue log, lessons learned register, physical resource assignments, project schedule, resource breakdown structure, resource requirements, risk register)",
                                         "Work performance data",
                                         "Agreements",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Data analysis (alternatives analysis, cost-benefit analysis, performance reviews, trend analysis)",
                                                   "Problem solving",
                                                   "Interpersonal and team skills (negotiation, influencing)",
                                                   "Project management information system (PMIS)"
                                               ],
                          "outputs":  [
                                          "Work performance information",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Control Resources focuses on PHYSICAL resources (equipment, materials, facilities)",
                                             "Manage Team focuses on HUMAN resources (people)",
                                             "Resource shortages may require schedule changes or alternative resources",
                                             "Trend analysis helps predict future resource needs"
                                         ],
                          "agile_considerations":  [
                                                       "Team capacity is monitored through velocity trends",
                                                       "Impediments that block resources are escalated quickly"
                                                   ]
                      }
                  ],
    "key_formulas":  [

                     ],
    "exam_tips":  [
                      "Know the difference between Develop Team (improve skills) and Manage Team (day-to-day)",
                      "RACI: Only ONE A (Accountable) per task, but can have multiple R (Responsible)",
                      "Tuckman\u0027s stages: Forming → Storming → Norming → Performing → Adjourning",
                      "Conflict resolution: Collaborate is best, Force is worst (but needed in emergencies)",
                      "Resource calendars show availability; RBS shows hierarchy of resources",
                      "Pre-assignment happens when resources are named in charter or contract",
                      "Team charter establishes operating guidelines — create it early!"
                  ]
}

STUDY_GUIDES['communications-management'] = {
    "id":  "communications-management",
    "name":  "Project Communications Management",
    "description":  "Includes the processes required to ensure that the information needs of the project and its stakeholders are met through timely and appropriate planning, collection, creation, distribution, storage, retrieval, management, control, monitoring, and ultimate disposition of project information.",
    "processes":  [
                      {
                          "id":  "10.1",
                          "name":  "Plan Communications Management",
                          "process_group":  "Planning",
                          "description":  "The process of developing an appropriate approach and plan for project communications based on stakeholder\u0027s information needs and requirements, and available organizational assets.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan (resource management plan, stakeholder engagement plan)",
                                         "Project documents (requirements documentation, stakeholder register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Communication requirements analysis",
                                                   "Communication technology",
                                                   "Communication methods",
                                                   "Communication models",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Communications management plan",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Communication channels formula: n(n-1)/2 where n = number of stakeholders",
                                             "5C\u0027s of communication: Correct, Concise, Clear, Coherent, Controlling",
                                             "Communication methods: Interactive (dialogue), Push (sent), Pull (accessed)",
                                             "The communications management plan is part of the project management plan"
                                         ],
                          "agile_considerations":  [
                                                       "Daily stand-ups are primary communication method in Scrum",
                                                       "Information radiators (boards, charts) make communication transparent",
                                                       "Face-to-face communication is preferred in agile"
                                                   ]
                      },
                      {
                          "id":  "10.2",
                          "name":  "Manage Communications",
                          "process_group":  "Executing",
                          "description":  "The process of ensuring timely and appropriate collection, creation, distribution, storage, retrieval, management, monitoring, and the ultimate disposition of project information.",
                          "inputs":  [
                                         "Project management plan (resource management plan, communications management plan, stakeholder engagement plan)",
                                         "Project documents (change log, issue log, lessons learned register, quality report, risk report, stakeholder register)",
                                         "Work performance reports",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Communication technology",
                                                   "Communication methods",
                                                   "Communication skills (communication competence, feedback, nonverbal, presentations)",
                                                   "Project management information system (PMIS)",
                                                   "Project reporting",
                                                   "Interpersonal and team skills (active listening, conflict management, cultural awareness, meeting management, networking, political awareness)"
                                               ],
                          "outputs":  [
                                          "Project communications",
                                          "Project management plan updates",
                                          "Project documents updates",
                                          "Organizational process assets updates"
                                      ],
                          "exam_traps":  [
                                             "Manage Communications = EXECUTING communications as planned",
                                             "Effective communication = 55% nonverbal + 38% vocal + 7% words (Mehrabian\u0027s rule)",
                                             "Feedback ensures message was understood correctly",
                                             "Project reporting includes status reports, progress measurements, and forecasts"
                                         ],
                          "agile_considerations":  [
                                                       "Daily stand-ups, sprint reviews, and retrospectives are key communication events",
                                                       "Collaboration tools support distributed agile teams"
                                                   ]
                      },
                      {
                          "id":  "10.3",
                          "name":  "Monitor Communications",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of ensuring the information needs of the project and its stakeholders are met.",
                          "inputs":  [
                                         "Project management plan (resource management plan, communications management plan, stakeholder engagement plan)",
                                         "Project documents (issue log, lessons learned register, project communications)",
                                         "Work performance data",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Project management information system (PMIS)",
                                                   "Data analysis (stakeholder engagement assessment)",
                                                   "Interpersonal and team skills (observation/conversation)"
                                               ],
                          "outputs":  [
                                          "Work performance information",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Monitor Communications ensures communications are EFFECTIVE and TIMELY",
                                             "If stakeholders aren\u0027t responding, the communications plan may need adjustment",
                                             "Communication problems are a frequent source of project issues"
                                         ],
                          "agile_considerations":  [
                                                       "Communication effectiveness is assessed through team feedback",
                                                       "Information radiators help identify communication gaps"
                                                   ]
                      }
                  ],
    "key_formulas":  [
                         {
                             "name":  "Communication Channels",
                             "formulas":  [
                                              "Communication Channels = n(n-1)/2",
                                              "Where n = number of stakeholders (including project manager)"
                                          ]
                         }
                     ],
    "exam_tips":  [
                      "Communication channels grow exponentially — a 10-person team has 45 channels",
                      "Interactive communication (meetings, calls) is best for complex issues",
                      "Push communication (emails, memos) ensures delivery but not understanding",
                      "Pull communication (intranet, databases) works best for large volumes of information",
                      "Nonverbal communication (55%) is more important than words (7%)",
                      "Active listening = pay attention, acknowledge, clarify, confirm understanding",
                      "Communication problems are the #1 cause of project issues — plan carefully!"
                  ]
}

STUDY_GUIDES['risk-management'] = {
    "id":  "risk-management",
    "name":  "Project Risk Management",
    "description":  "Includes the processes of conducting risk management planning, identification, analysis, response planning, response implementation, and monitoring risk on a project.",
    "processes":  [
                      {
                          "id":  "11.1",
                          "name":  "Plan Risk Management",
                          "process_group":  "Planning",
                          "description":  "The process of defining how to conduct risk management activities for a project.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan (all components)",
                                         "Project documents (stakeholder register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data analysis (stakeholder analysis)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Risk management plan"
                                      ],
                          "exam_traps":  [
                                             "The risk management plan is part of the project management plan",
                                             "It defines methodology, roles, budget, timing, risk categories, probability/impact matrix, stakeholder risk appetite, reporting formats, and tracking",
                                             "Risk appetite = amount of risk an organization is willing to accept",
                                             "Risk threshold = the level at which risk becomes unacceptable"
                                         ],
                          "agile_considerations":  [
                                                       "Risk management is integrated into iteration planning and retrospectives",
                                                       "Short iterations reduce risk exposure time"
                                                   ]
                      },
                      {
                          "id":  "11.2",
                          "name":  "Identify Risks",
                          "process_group":  "Planning",
                          "description":  "The process of identifying individual project risks as well as sources of overall project risk, and documenting their characteristics.",
                          "inputs":  [
                                         "Project management plan (requirements management plan, schedule management plan, cost management plan, quality management plan, resource management plan, risk management plan, scope baseline, schedule baseline, cost baseline)",
                                         "Project documents (assumption log, change log, issue log, lessons learned register, requirements documentation, resource requirements, stakeholder register)",
                                         "Agreements",
                                         "Procurement documentation",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (brainstorming, checklists, interviews)",
                                                   "Data analysis (root cause analysis, assumption and constraint analysis, SWOT analysis, document analysis)",
                                                   "Interpersonal and team skills (facilitation)",
                                                   "Prompt lists",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Risk register",
                                          "Risk report",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Risks can be positive (opportunities) or negative (threats)",
                                             "The risk register is created in Identify Risks and updated throughout",
                                             "Risk categories help organize risks (RBS = Risk Breakdown Structure)",
                                             "SWOT analysis identifies Strengths, Weaknesses, Opportunities, Threats",
                                             "Root cause analysis finds the underlying source of risks"
                                         ],
                          "agile_considerations":  [
                                                       "Risks are identified during iteration planning and daily stand-ups",
                                                       "Spikes are used to reduce technical risks"
                                                   ]
                      },
                      {
                          "id":  "11.3",
                          "name":  "Perform Qualitative Risk Analysis",
                          "process_group":  "Planning",
                          "description":  "The process of prioritizing individual project risks for further analysis or action by assessing their probability of occurrence and impact as well as other characteristics.",
                          "inputs":  [
                                         "Project management plan (risk management plan)",
                                         "Project documents (assumption log, risk register, stakeholder register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (interviews)",
                                                   "Data analysis (risk data quality assessment, risk probability and impact assessment, assessment of other risk parameters, probability and impact matrix, hierarchical charts)",
                                                   "Interpersonal and team skills (facilitation)",
                                                   "Risk categorization",
                                                   "Data representation (probability and impact matrix, hierarchical charts)"
                                               ],
                          "outputs":  [
                                          "Project documents updates (risk register updates)"
                                      ],
                          "exam_traps":  [
                                             "Qualitative = subjective assessment using probability and impact",
                                             "Probability/Impact matrix helps prioritize risks (High/Medium/Low)",
                                             "Risk score = Probability × Impact",
                                             "Urgency, proximity, dormancy, manageability, controllability are other factors",
                                             "Data quality assessment evaluates reliability of risk data"
                                         ],
                          "agile_considerations":  [
                                                       "Risks are prioritized in iteration planning based on impact",
                                                       "High-priority risks are addressed first in the backlog"
                                                   ]
                      },
                      {
                          "id":  "11.4",
                          "name":  "Perform Quantitative Risk Analysis",
                          "process_group":  "Planning",
                          "description":  "The process of numerically analyzing the effect of identified individual project risks and other sources of uncertainty on overall project objectives.",
                          "inputs":  [
                                         "Project management plan (risk management plan, scope baseline, schedule baseline, cost baseline)",
                                         "Project documents (assumption log, basis of estimates, cost estimates, cost forecasts, duration estimates, milestone list, resource requirements, risk register, risk report, schedule forecasts)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (interviews)",
                                                   "Interpersonal and team skills (facilitation)",
                                                   "Representation of uncertainty",
                                                   "Data analysis (simulation, sensitivity analysis, decision tree analysis, influence diagrams)"
                                               ],
                          "outputs":  [
                                          "Project documents updates (risk register updates)"
                                      ],
                          "exam_traps":  [
                                             "Quantitative = NUMERICAL analysis (not always performed)",
                                             "Monte Carlo simulation runs thousands of iterations to predict outcomes",
                                             "Sensitivity analysis (tornado diagram) shows which risks have the most impact",
                                             "Decision tree analysis calculates Expected Monetary Value (EMV)",
                                             "EMV = Probability × Impact (use for both threats and opportunities)",
                                             "NOT all projects need quantitative analysis — it\u0027s optional"
                                         ],
                          "agile_considerations":  [
                                                       "Quantitative analysis may be simplified in agile due to short iterations",
                                                       "Velocity variance can be modeled probabilistically"
                                                   ]
                      },
                      {
                          "id":  "11.5",
                          "name":  "Plan Risk Responses",
                          "process_group":  "Planning",
                          "description":  "The process of developing options, selecting strategies, and agreeing on actions to address overall project risk exposure, as well as to treat individual project risks.",
                          "inputs":  [
                                         "Project management plan (resource management plan, risk management plan, cost baseline)",
                                         "Project documents (lessons learned register, project schedule, project team assignments, resource calendars, risk register, risk report, stakeholder register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (interviews)",
                                                   "Interpersonal and team skills (facilitation)",
                                                   "Strategies for threats (escalate, avoid, transfer, mitigate, accept)",
                                                   "Strategies for opportunities (escalate, exploit, share, enhance, accept)",
                                                   "Contingent response strategies",
                                                   "Data analysis (alternatives analysis, cost-benefit analysis, multicriteria decision analysis)"
                                               ],
                          "outputs":  [
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "THREAT strategies: Escalate (wrong level), Avoid (eliminate threat), Transfer (shift impact), Mitigate (reduce probability/impact), Accept (passive or active)",
                                             "OPPORTUNITY strategies: Escalate (wrong level), Exploit (ensure it happens), Share (partner), Enhance (increase probability/impact), Accept (passive)",
                                             "Contingent responses (fallback plans) are activated when triggers occur",
                                             "Secondary risks are risks that arise from implementing a risk response"
                                         ],
                          "agile_considerations":  [
                                                       "Risk responses are built into iteration planning",
                                                       "Spikes are a form of risk mitigation for technical uncertainty"
                                                   ]
                      },
                      {
                          "id":  "11.6",
                          "name":  "Implement Risk Responses",
                          "process_group":  "Executing",
                          "description":  "The process of implementing agreed-upon risk response plans.",
                          "inputs":  [
                                         "Project management plan (risk management plan)",
                                         "Project documents (lessons learned register, risk register, risk report)",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Interpersonal and team skills (influencing)"
                                               ],
                          "outputs":  [
                                          "Change requests",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Implement Risk Responses is an EXECUTING process — take action!",
                                             "Risk owners are responsible for implementing agreed responses",
                                             "Responses must be executed according to the risk management plan"
                                         ],
                          "agile_considerations":  [
                                                       "Risk responses are executed during iterations as part of normal work",
                                                       "Risk burndown charts track risk exposure over time"
                                                   ]
                      },
                      {
                          "id":  "11.7",
                          "name":  "Monitor Risks",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of monitoring the implementation of agreed-upon risk response plans, tracking identified risks, identifying and analyzing new risks, and evaluating risk process effectiveness throughout the project.",
                          "inputs":  [
                                         "Project management plan (risk management plan)",
                                         "Project documents (issue log, lessons learned register, risk register, risk report)",
                                         "Work performance data",
                                         "Work performance reports"
                                     ],
                          "tools_techniques":  [
                                                   "Data analysis (technical performance analysis, reserve analysis)",
                                                   "Audits",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Work performance information",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates",
                                          "Organizational process assets updates"
                                      ],
                          "exam_traps":  [
                                             "Reserve analysis compares actual contingency reserve usage to planned",
                                             "Risk audits examine effectiveness of risk responses",
                                             "New risks may emerge at any time — risk management is continuous",
                                             "If a risk is realized, execute the contingency plan (if one exists)"
                                         ],
                          "agile_considerations":  [
                                                       "Risks are monitored daily in stand-ups",
                                                       "Risk burn-down charts show risk exposure over iterations"
                                                   ]
                      }
                  ],
    "key_formulas":  [
                         {
                             "name":  "Expected Monetary Value (EMV)",
                             "formulas":  [
                                              "EMV = Probability × Impact",
                                              "Positive EMV = opportunity value",
                                              "Negative EMV = threat cost"
                                          ]
                         }
                     ],
    "exam_tips":  [
                      "ALWAYS consider both threats AND opportunities — not just negative risks",
                      "Risk register is created in Identify Risks and updated in EVERY subsequent process",
                      "Qualitative analysis prioritizes; Quantitative analysis quantifies (optional)",
                      "Threat strategies: Escalate, Avoid, Transfer, Mitigate, Accept",
                      "Opportunity strategies: Escalate, Exploit, Share, Enhance, Accept",
                      "Transfer = insurance, warranties, guarantees, bonds, contracts",
                      "Mitigate = reduce probability OR impact (or both)",
                      "Exploit = do everything to make an opportunity happen",
                      "Monte Carlo = simulation; Tornado diagram = sensitivity analysis",
                      "Secondary risks arise from risk responses — plan for them too!"
                  ]
}

STUDY_GUIDES['procurement-management'] = {
    "id":  "procurement-management",
    "name":  "Project Procurement Management",
    "description":  "Includes the processes necessary to purchase or acquire products, services, or results needed from outside the project team.",
    "processes":  [
                      {
                          "id":  "12.1",
                          "name":  "Plan Procurement Management",
                          "process_group":  "Planning",
                          "description":  "The process of documenting project procurement decisions, specifying the approach, and identifying potential sellers.",
                          "inputs":  [
                                         "Project charter",
                                         "Business documents (business case, benefits management plan)",
                                         "Project management plan (scope management plan, quality management plan, resource management plan, scope baseline)",
                                         "Project documents (milestone list, project team assignments, requirements documentation, requirements traceability matrix, resource requirements, risk register, stakeholder register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (market research)",
                                                   "Data analysis (make-or-buy analysis)",
                                                   "Source selection analysis"
                                               ],
                          "outputs":  [
                                          "Procurement management plan",
                                          "Procurement strategy",
                                          "Bid documents",
                                          "Procurement statement of work",
                                          "Source selection criteria",
                                          "Make-or-buy decisions",
                                          "Independent cost estimates",
                                          "Change requests",
                                          "Project documents updates",
                                          "Organizational process assets updates"
                                      ],
                          "exam_traps":  [
                                             "Make-or-buy analysis considers cost, capacity, expertise, and strategic value",
                                             "Procurement SOW describes what to be procured, NOT how",
                                             "Bid documents include RFI (Request for Information), RFP (Request for Proposal), RFQ (Request for Quotation)",
                                             "Source selection criteria define how sellers will be evaluated",
                                             "Independent cost estimates verify reasonableness of seller proposals"
                                         ],
                          "agile_considerations":  [
                                                       "Agile contracts may use time-and-materials or incremental delivery",
                                                       "Customer collaboration is emphasized over contract negotiation"
                                                   ]
                      },
                      {
                          "id":  "12.2",
                          "name":  "Conduct Procurements",
                          "process_group":  "Executing",
                          "description":  "The process of obtaining seller responses, selecting a seller, and awarding a contract.",
                          "inputs":  [
                                         "Project management plan (scope management plan, requirements management plan, communications management plan, risk management plan, procurement management plan, cost baseline, configuration management plan)",
                                         "Project documents (lessons learned register, project schedule, requirements documentation, risk register, stakeholder register)",
                                         "Procurement documentation",
                                         "Seller proposals",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Advertising",
                                                   "Bidder conferences",
                                                   "Data analysis (proposal evaluation)",
                                                   "Interpersonal and team skills (negotiation)"
                                               ],
                          "outputs":  [
                                          "Selected sellers",
                                          "Agreements",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates",
                                          "Organizational process assets updates"
                                      ],
                          "exam_traps":  [
                                             "Bidder conferences ensure all sellers have same information (fairness)",
                                             "Negotiation clarifies structure, requirements, and terms before signing",
                                             "Agreements are legally binding contracts — formal and detailed",
                                             "Selected sellers are those who have been chosen to provide the product/service",
                                             "Proposal evaluation uses source selection criteria defined earlier"
                                         ],
                          "agile_considerations":  [
                                                       "Agile procurement may involve shorter contracts with more frequent reviews",
                                                       "Collaborative partnerships are preferred over adversarial relationships"
                                                   ]
                      },
                      {
                          "id":  "12.3",
                          "name":  "Control Procurements",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of managing procurement relationships, monitoring contract performance, making changes and corrections as appropriate, and closing out contracts.",
                          "inputs":  [
                                         "Project management plan (requirements management plan, risk management plan, procurement management plan, change management plan, schedule baseline)",
                                         "Project documents (assumption log, lessons learned register, milestone list, quality reports, requirements documentation, requirements traceability matrix, risk register, stakeholder register)",
                                         "Agreements",
                                         "Procurement documentation",
                                         "Approved change requests",
                                         "Work performance data",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Claims administration",
                                                   "Data analysis (performance reviews, earned value analysis, trend analysis)",
                                                   "Inspection",
                                                   "Audits"
                                               ],
                          "outputs":  [
                                          "Closed procurements",
                                          "Work performance information",
                                          "Procurement documentation updates",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates",
                                          "Organizational process assets updates"
                                      ],
                          "exam_traps":  [
                                             "Control Procurements ensures both buyer AND seller meet contractual obligations",
                                             "Claims administration handles disputes — negotiate first, then ADR, then litigation",
                                             "Alternative Dispute Resolution (ADR) includes mediation and arbitration",
                                             "Inspections verify deliverables meet requirements",
                                             "Audits review procurement processes for compliance",
                                             "Contract changes must go through formal change control"
                                         ],
                          "agile_considerations":  [
                                                       "Agile contracts may allow scope flexibility within fixed time/cost",
                                                       "Regular retrospectives with vendors improve collaboration"
                                                   ]
                      }
                  ],
    "key_formulas":  [

                     ],
    "exam_tips":  [
                      "Plan Procurement = decide what to buy, how to buy, and when",
                      "Conduct Procurements = get proposals, evaluate, negotiate, award",
                      "Control Procurements = monitor performance, handle changes, close contracts",
                      "Make-or-buy analysis: consider cost, capacity, control, confidentiality",
                      "RFP = Request for Proposal (solutions), RFQ = Request for Quotation (price)",
                      "Bidder conferences ensure fairness — all sellers get same info",
                      "Claims = disputes; resolve through negotiation → ADR → litigation",
                      "Contract types: Fixed-price (seller risk), Cost-reimbursable (buyer risk), Time-and-materials (shared risk)",
                      "Firm Fixed Price (FFP) = most risk to seller; Cost Plus Fixed Fee (CPFF) = most risk to buyer"
                  ]
}

STUDY_GUIDES['stakeholder-management'] = {
    "id":  "stakeholder-management",
    "name":  "Project Stakeholder Management",
    "description":  "Includes the processes required to identify the people, groups, or organizations that could impact or be impacted by the project, to analyze stakeholder expectations and their impact on the project, and to develop appropriate management strategies for effectively engaging stakeholders in project decisions and execution.",
    "processes":  [
                      {
                          "id":  "13.1",
                          "name":  "Identify Stakeholders",
                          "process_group":  "Initiating",
                          "description":  "The process of identifying project stakeholders regularly and analyzing and documenting relevant information regarding their interests, involvement, interdependencies, influence, and potential impact on project success.",
                          "inputs":  [
                                         "Project charter",
                                         "Business documents (business case, benefits management plan)",
                                         "Project management plan (communications management plan, stakeholder engagement plan)",
                                         "Project documents (change log, issue log, requirements documentation)",
                                         "Agreements",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (questionnaires and surveys, brainstorming)",
                                                   "Data analysis (stakeholder analysis, document analysis)",
                                                   "Data representation (stakeholder mapping/representation)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Stakeholder register",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates",
                                          "Enterprise environmental factors updates",
                                          "Organizational process assets updates"
                                      ],
                          "exam_traps":  [
                                             "Stakeholder register is created in Initiating and updated throughout",
                                             "Power/Interest grid: High Power + High Interest = Manage Closely; Low Power + Low Interest = Monitor",
                                             "Salience model considers power, urgency, and legitimacy",
                                             "Don\u0027t forget INTERNAL stakeholders (team, management) AND EXTERNAL (customers, regulators)",
                                             "Stakeholder identification is continuous — new stakeholders emerge throughout"
                                         ],
                          "agile_considerations":  [
                                                       "Product owner is a key stakeholder representing customer needs",
                                                       "Stakeholders participate in sprint reviews and provide feedback"
                                                   ]
                      },
                      {
                          "id":  "13.2",
                          "name":  "Plan Stakeholder Engagement",
                          "process_group":  "Planning",
                          "description":  "The process of developing approaches to involve project stakeholders based on their needs, expectations, interests, and potential impact on the project.",
                          "inputs":  [
                                         "Project charter",
                                         "Project management plan (resource management plan, communications management plan, risk management plan)",
                                         "Project documents (assumption log, change log, issue log, project schedule, risk register, stakeholder register)",
                                         "Agreements",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Data gathering (benchmarking)",
                                                   "Data analysis (assumption and constraint analysis, root cause analysis)",
                                                   "Decision making (prioritization/ranking)",
                                                   "Data representation (mind mapping, stakeholder engagement assessment matrix)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Stakeholder engagement plan"
                                      ],
                          "exam_traps":  [
                                             "Stakeholder engagement plan defines HOW to engage stakeholders, not who they are",
                                             "Stakeholder engagement assessment matrix compares current vs. desired engagement levels",
                                             "Engagement levels: Unaware → Resistant → Neutral → Supportive → Leading",
                                             "The plan is part of the project management plan"
                                         ],
                          "agile_considerations":  [
                                                       "High collaboration and transparency reduce stakeholder resistance",
                                                       "Regular demos and reviews keep stakeholders engaged"
                                                   ]
                      },
                      {
                          "id":  "13.3",
                          "name":  "Manage Stakeholder Engagement",
                          "process_group":  "Executing",
                          "description":  "The process of communicating and working with stakeholders to meet their needs and expectations, address issues, and foster appropriate stakeholder involvement.",
                          "inputs":  [
                                         "Project management plan (communications management plan, risk management plan, stakeholder engagement plan, change management plan)",
                                         "Project documents (change log, issue log, lessons learned register, stakeholder register)",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Expert judgment",
                                                   "Communication skills (feedback)",
                                                   "Interpersonal and team skills (conflict management, cultural awareness, negotiation, observation/conversation, political awareness)",
                                                   "Ground rules",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates",
                                          "Enterprise environmental factors updates"
                                      ],
                          "exam_traps":  [
                                             "Manage Stakeholder Engagement = actively work WITH stakeholders",
                                             "Address concerns before they become issues",
                                             "Ground rules establish acceptable behavior for stakeholder interactions",
                                             "Political awareness helps navigate organizational politics",
                                             "Cultural awareness is critical for global/virtual teams"
                                         ],
                          "agile_considerations":  [
                                                       "Daily collaboration with product owner ensures stakeholder needs are met",
                                                       "Sprint reviews provide regular stakeholder engagement opportunities"
                                                   ]
                      },
                      {
                          "id":  "13.4",
                          "name":  "Monitor Stakeholder Engagement",
                          "process_group":  "Monitoring and Controlling",
                          "description":  "The process of monitoring project stakeholder relationships and tailoring strategies for engaging stakeholders through modification of engagement strategies and plans.",
                          "inputs":  [
                                         "Project management plan (resource management plan, communications management plan, stakeholder engagement plan)",
                                         "Project documents (issue log, lessons learned register, project communications, risk register, stakeholder register)",
                                         "Work performance data",
                                         "Enterprise environmental factors",
                                         "Organizational process assets"
                                     ],
                          "tools_techniques":  [
                                                   "Data analysis (alternatives analysis, root cause analysis, stakeholder engagement assessment matrix)",
                                                   "Decision making (multicriteria decision analysis, voting)",
                                                   "Communication skills (feedback, presentations)",
                                                   "Interpersonal and team skills (active listening, cultural awareness, leadership, networking, political awareness)",
                                                   "Meetings"
                                               ],
                          "outputs":  [
                                          "Work performance information",
                                          "Change requests",
                                          "Project management plan updates",
                                          "Project documents updates"
                                      ],
                          "exam_traps":  [
                                             "Monitor Stakeholder Engagement ensures strategies are EFFECTIVE",
                                             "If stakeholders are becoming resistant, adjust engagement strategies",
                                             "Compare current vs. desired engagement levels regularly",
                                             "Stakeholder satisfaction is a key project success criterion"
                                         ],
                          "agile_considerations":  [
                                                       "Stakeholder feedback from reviews drives backlog prioritization",
                                                       "Retrospectives assess stakeholder engagement effectiveness"
                                                   ]
                      }
                  ],
    "key_formulas":  [

                     ],
    "exam_tips":  [
                      "Identify Stakeholders = Initiating (create register)",
                      "Plan Stakeholder Engagement = Planning (define strategies)",
                      "Manage Stakeholder Engagement = Executing (work with stakeholders)",
                      "Monitor Stakeholder Engagement = Monitoring (check effectiveness)",
                      "Power/Interest grid is the most common stakeholder analysis tool",
                      "High Power + High Interest = Manage Closely (most important)",
                      "Stakeholder engagement levels: Unaware → Resistant → Neutral → Supportive → Leading",
                      "Address stakeholder concerns early — resistance grows if ignored",
                      "Political and cultural awareness are critical for stakeholder management",
                      "Stakeholder satisfaction is a primary measure of project success"
                  ]
}
