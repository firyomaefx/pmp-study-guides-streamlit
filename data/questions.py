QUESTIONS = [
  {
    "id": "PMP001",
    "domain": "process",
    "knowledge_area": "integration-management",
    "process_group": "initiating",
    "difficulty": "easy",
    "question_type": "multiple_choice",
    "scenario": "A project manager has been assigned to a new software development project. The organization is using a hybrid approach with both predictive and agile elements.",
    "question": "What document formally authorizes the existence of the project and provides the project manager with the authority to apply organizational resources to project activities?",
    "options": [
      {"id": "A", "text": "Project Management Plan"},
      {"id": "B", "text": "Project Charter"},
      {"id": "C", "text": "Statement of Work"},
      {"id": "D", "text": "Business Case"}
    ],
    "correct_answer": "B",
    "explanation": "The Project Charter is the document that formally authorizes the existence of a project and provides the project manager with the authority to apply organizational resources to project activities. The Project Management Plan (A) is created after the charter. The Statement of Work (C) describes the product scope. The Business Case (D) justifies the project but doesn't authorize it.",
    "references": ["PMBOK 6th Ed, Section 4.1"],
    "skills_tested": ["develop_project_charter"]
  },
  {
    "id": "PMP002",
    "domain": "process",
    "knowledge_area": "integration-management",
    "process_group": "planning",
    "difficulty": "medium",
    "question_type": "multiple_choice",
    "scenario": "During project planning, the project team is developing the detailed project management plan. Several subsidiary plans have been created by different team members.",
    "question": "Which of the following is NOT a subsidiary plan that would be included in the Project Management Plan?",
    "options": [
      {"id": "A", "text": "Scope Management Plan"},
      {"id": "B", "text": "Requirements Management Plan"},
      {"id": "C", "text": "Project Charter"},
      {"id": "D", "text": "Cost Management Plan"}
    ],
    "correct_answer": "C",
    "explanation": "The Project Charter is NOT a subsidiary plan of the Project Management Plan. It is a separate document that formally authorizes the project. The Scope Management Plan (A), Requirements Management Plan (B), and Cost Management Plan (D) are all valid subsidiary plans that make up the comprehensive Project Management Plan.",
    "references": ["PMBOK 6th Ed, Section 4.2"],
    "skills_tested": ["develop_project_management_plan"]
  },
  {
    "id": "PMP003",
    "domain": "process",
    "knowledge_area": "integration-management",
    "process_group": "executing",
    "difficulty": "medium",
    "question_type": "multiple_choice",
    "scenario": "The project team is executing the project work as defined in the project management plan. During execution, the team discovers that a deliverable needs minor correction to meet quality standards.",
    "question": "What should the project manager do FIRST when a deliverable needs correction during project execution?",
    "options": [
      {"id": "A", "text": "Implement the correction immediately to maintain schedule"},
      {"id": "B", "text": "Submit a change request through the Perform Integrated Change Control process"},
      {"id": "C", "text": "Update the project management plan with the correction"},
      {"id": "D", "text": "Inform the project sponsor and wait for approval"}
    ],
    "correct_answer": "B",
    "explanation": "When any correction, update, or change is needed during project execution, a change request must be submitted through the Perform Integrated Change Control process. Implementing corrections immediately (A) bypasses change control. Updating the plan directly (C) violates the change control process. While informing the sponsor (D) is good practice, the formal change request process must be followed.",
    "references": ["PMBOK 6th Ed, Section 4.6"],
    "skills_tested": ["perform_integrated_change_control"]
  },
  {
    "id": "PMP004",
    "domain": "process",
    "knowledge_area": "integration-management",
    "process_group": "monitoring_controlling",
    "difficulty": "hard",
    "question_type": "multiple_choice",
    "scenario": "A project is 6 months into execution. The project manager is reviewing performance reports and notices that the Cost Performance Index (CPI) is 0.85 and the Schedule Performance Index (SPI) is 1.10. The project has a Budget at Completion (BAC) of $500,000.",
    "question": "Based on the current performance, what is the Estimate at Completion (EAC) if the current cost trends are expected to continue?",
    "options": [
      {"id": "A", "text": "$500,000"},
      {"id": "B", "text": "$588,235"},
      {"id": "C", "text": "$450,000"},
      {"id": "D", "text": "$550,000"}
    ],
    "correct_answer": "B",
    "explanation": "If current cost trends continue, EAC = BAC / CPI. With BAC = $500,000 and CPI = 0.85: EAC = $500,000 / 0.85 = $588,235. Option A ($500,000) would be correct if both CPI and SPI were 1.0. Option C assumes costs will improve. Option D is not a valid EVM calculation.",
    "references": ["PMBOK 6th Ed, Section 7.4"],
    "skills_tested": ["earned_value_management", "estimate_at_completion"]
  },
  {
    "id": "PMP005",
    "domain": "people",
    "knowledge_area": "integration-management",
    "process_group": "closing",
    "difficulty": "easy",
    "question_type": "multiple_choice",
    "scenario": "A project to develop a new mobile application has been completed. All deliverables have been accepted by the customer, and the final report has been distributed to stakeholders.",
    "question": "What is the PRIMARY purpose of updating Organizational Process Assets (OPAs) at project closure?",
    "options": [
      {"id": "A", "text": "To meet contractual requirements with the customer"},
      {"id": "B", "text": "To transfer knowledge and lessons learned to future projects"},
      {"id": "C", "text": "To release project team members for other assignments"},
      {"id": "D", "text": "To close the project procurement contracts"}
    ],
    "correct_answer": "B",
    "explanation": "The primary purpose of updating OPAs at closure is to transfer knowledge, lessons learned, and project files to benefit future projects. While meeting contractual requirements (A) and closing contracts (D) are important, they are not the primary purpose of OPA updates. Releasing team members (C) is an administrative activity but unrelated to OPAs.",
    "references": ["PMBOK 6th Ed, Section 4.7"],
    "skills_tested": ["close_project_or_phase"]
  },
  {
    "id": "PMP006",
    "domain": "process",
    "knowledge_area": "scope-management",
    "process_group": "planning",
    "difficulty": "easy",
    "question_type": "multiple_choice",
    "scenario": "During the planning phase of a construction project, the project team is working to clearly define what work is included and excluded from the project.",
    "question": "Which document contains the detailed description of the project and product, including deliverables, acceptance criteria, exclusions, constraints, and assumptions?",
    "options": [
      {"id": "A", "text": "Work Breakdown Structure (WBS)"},
      {"id": "B", "text": "Project Scope Statement"},
      {"id": "C", "text": "Requirements Traceability Matrix"},
      {"id": "D", "text": "Scope Management Plan"}
    ],
    "correct_answer": "B",
    "explanation": "The Project Scope Statement contains the detailed description of the project and product, including deliverables, acceptance criteria, exclusions, constraints, and assumptions. The WBS (A) is the hierarchical decomposition of work. The RTM (C) links requirements to deliverables. The Scope Management Plan (D) describes HOW scope will be managed, not the actual scope.",
    "references": ["PMBOK 6th Ed, Section 5.3"],
    "skills_tested": ["define_scope"]
  },
  {
    "id": "PMP007",
    "domain": "process",
    "knowledge_area": "scope-management",
    "process_group": "planning",
    "difficulty": "medium",
    "question_type": "multiple_choice",
    "scenario": "A software development team is creating the Work Breakdown Structure for a new e-commerce platform. The project manager wants to ensure all work is accounted for without including unnecessary activities.",
    "question": "What is the key principle that ensures the WBS includes 100% of the work defined by the project scope and captures ALL deliverables?",
    "options": [
      {"id": "A", "text": "Rolling Wave Planning"},
      {"id": "B", "text": "The 100% Rule"},
      {"id": "C", "text": "Progressive Elaboration"},
      {"id": "D", "text": "Decomposition"}
    ],
    "correct_answer": "B",
    "explanation": "The 100% Rule states that the WBS includes 100% of the work defined by the project scope and captures all deliverables, including internal and external. Rolling Wave Planning (A) is a form of progressive elaboration for future work. Progressive Elaboration (C) is the iterative process of increasing detail. Decomposition (D) is the technique used to create the WBS but doesn't ensure completeness.",
    "references": ["PMBOK 6th Ed, Section 5.4"],
    "skills_tested": ["create_wbs"]
  },
  {
    "id": "PMP008",
    "domain": "process",
    "knowledge_area": "scope-management",
    "process_group": "monitoring_controlling",
    "difficulty": "hard",
    "question_type": "multiple_choice",
    "scenario": "During a project's execution, the customer requests an additional feature that was not originally included in the scope. The project team believes this feature would significantly improve the product and wants to add it.",
    "question": "The project manager should treat this request as an example of:",
    "options": [
      {"id": "A", "text": "Scope Creep - uncontrolled expansion of scope"},
      {"id": "B", "text": "Gold Plating - adding extra features not in scope"},
      {"id": "C", "text": "Progressive Elaboration - refining scope details"},
      {"id": "D", "text": "Scope Baseline Update - normal scope refinement"}
    ],
    "correct_answer": "A",
    "explanation": "A customer requesting additional features not in the original scope is Scope Creep - the uncontrolled expansion of project scope without proper change control. Gold Plating (B) is when the TEAM adds extra features voluntarily. Progressive Elaboration (C) is about refining details of already-approved scope. Scope Baseline Update (D) requires formal change control.",
    "references": ["PMBOK 6th Ed, Section 5.6"],
    "skills_tested": ["control_scope", "scope_creep"]
  },
  {
    "id": "PMP009",
    "domain": "process",
    "knowledge_area": "scope-management",
    "process_group": "monitoring_controlling",
    "difficulty": "medium",
    "question_type": "multiple_choice",
    "scenario": "A deliverable has been completed by the project team. Before presenting it to the customer for acceptance, the project manager wants to ensure it meets the quality requirements specified in the project scope.",
    "question": "Which process should be completed FIRST before the deliverable is presented to the customer for formal acceptance?",
    "options": [
      {"id": "A", "text": "Validate Scope"},
      {"id": "B", "text": "Control Quality"},
      {"id": "C", "text": "Perform Integrated Change Control"},
      {"id": "D", "text": "Manage Stakeholder Engagement"}
    ],
    "correct_answer": "B",
    "explanation": "Control Quality (internal verification) should be completed BEFORE Validate Scope (external acceptance). The team must first ensure the deliverable meets quality standards internally before presenting it to the customer. Validate Scope (A) comes after Control Quality. The other options are not directly related to deliverable inspection.",
    "references": ["PMBOK 6th Ed, Sections 5.5 and 8.3"],
    "skills_tested": ["control_quality", "validate_scope"]
  },
  {
    "id": "PMP010",
    "domain": "people",
    "knowledge_area": "integration-management",
    "process_group": "executing",
    "difficulty": "medium",
    "question_type": "multiple_choice",
    "scenario": "A project manager is leading a team that includes members from three different departments and two external contractors. Communication has become challenging, and some team members feel left out of important decisions.",
    "question": "According to the PMBOK, which interpersonal skill is MOST important for the project manager to effectively manage this diverse team?",
    "options": [
      {"id": "A", "text": "Technical expertise in the project domain"},
      {"id": "B", "text": "Facilitation skills to ensure all voices are heard"},
      {"id": "C", "text": "Financial management skills to control costs"},
      {"id": "D", "text": "Programming skills to assist with technical work"}
    ],
    "correct_answer": "B",
    "explanation": "Facilitation skills are most important for ensuring all team members, including diverse stakeholders and contractors, can participate effectively in decision-making. Technical expertise (A) and programming skills (D) are less critical for a PM. Financial management (C) is important but doesn't address the communication and inclusion challenge described.",
    "references": ["PMBOK 6th Ed, Section 4.4"],
    "skills_tested": ["manage_project_knowledge", "facilitation"]
  },
  {
    "id": "PMP011",
    "domain": "process",
    "knowledge_area": "schedule-management",
    "process_group": "planning",
    "difficulty": "medium",
    "question_type": "multiple_choice",
    "scenario": "A project manager is developing the project schedule for a construction project. Several activities have dependencies that must be carefully sequenced.",
    "question": "In the Precedence Diagramming Method (PDM), what type of dependency exists when Activity B cannot start until Activity A has started?",
    "options": [
      {"id": "A", "text": "Finish-to-Start (FS)"},
      {"id": "B", "text": "Start-to-Start (SS)"},
      {"id": "C", "text": "Finish-to-Finish (FF)"},
      {"id": "D", "text": "Start-to-Finish (SF)"}
    ],
    "correct_answer": "B",
    "explanation": "Start-to-Start (SS) means Activity B cannot start until Activity A has started. Finish-to-Start (A) is when B cannot start until A finishes. Finish-to-Finish (C) means B cannot finish until A finishes. Start-to-Finish (D) means B cannot finish until A starts (rarely used).",
    "references": ["PMBOK 6th Ed, Section 6.3"],
    "skills_tested": ["sequence_activities"]
  },
  {
    "id": "PMP012",
    "domain": "process",
    "knowledge_area": "cost-management",
    "process_group": "planning",
    "difficulty": "hard",
    "question_type": "multiple_choice",
    "scenario": "A project has a Budget at Completion (BAC) of $200,000. At the current status date, the Earned Value (EV) is $80,000, the Actual Cost (AC) is $100,000, and the Planned Value (PV) is $90,000.",
    "question": "What is the To-Complete Performance Index (TCPI) based on the Budget at Completion?",
    "options": [
      {"id": "A", "text": "0.80"},
      {"id": "B", "text": "1.20"},
      {"id": "C", "text": "1.50"},
      {"id": "D", "text": "2.00"}
    ],
    "correct_answer": "B",
    "explanation": "TCPI = (BAC - EV) / (BAC - AC) = ($200,000 - $80,000) / ($200,000 - $100,000) = $120,000 / $100,000 = 1.20. A TCPI greater than 1.0 means the team needs to work more efficiently than originally planned to complete the project within the BAC.",
    "references": ["PMBOK 6th Ed, Section 7.4"],
    "skills_tested": ["earned_value_management", "tcpi"]
  },
  {
    "id": "PMP013",
    "domain": "process",
    "knowledge_area": "quality-management",
    "process_group": "executing",
    "difficulty": "easy",
    "question_type": "multiple_choice",
    "scenario": "A quality control inspector is examining manufactured parts to ensure they meet specifications. The inspector is using a checklist to verify each part against defined quality criteria.",
 "question": "What quality management process is being performed?",
    "options": [
      {"id": "A", "text": "Plan Quality Management"},
      {"id": "B", "text": "Manage Quality"},
      {"id": "C", "text": "Control Quality"},
      {"id": "D", "text": "Perform Quality Assurance"}
    ],
    "correct_answer": "C",
    "explanation": "Control Quality is the process of monitoring and recording results of executing quality management activities to assess performance and recommend necessary changes. It involves inspecting specific deliverables. Plan Quality Management (A) is the planning process. Manage Quality (B) [formerly Quality Assurance] focuses on processes. Perform Quality Assurance (D) is an older term for Manage Quality.",
    "references": ["PMBOK 6th Ed, Section 8.3"],
    "skills_tested": ["control_quality"]
  },
  {
    "id": "PMP014",
    "domain": "people",
    "knowledge_area": "resource-management",
    "process_group": "executing",
    "difficulty": "medium",
    "question_type": "multiple_choice",
    "scenario": "A project team is experiencing conflicts between two senior developers who have different technical approaches. The conflict is affecting team morale and productivity.",
    "question": "According to the PMBOK, what is the PRIMARY role of the project manager in managing team conflicts?",
    "options": [
      {"id": "A", "text": "Act as a judge to determine who is right"},
      {"id": "B", "text": "Facilitate a resolution that addresses the underlying issues"},
      {"id": "C", "text": "Escalate the conflict to senior management immediately"},
      {"id": "D", "text": "Reassign one of the developers to another project"}
    ],
    "correct_answer": "B",
    "explanation": "The PM's primary role is to facilitate a resolution that addresses underlying issues, not to judge who is right. Escalation (C) should only happen if the conflict cannot be resolved at the team level. Reassignment (D) avoids addressing the root cause. Effective conflict management leads to better team performance.",
    "references": ["PMBOK 6th Ed, Section 9.5"],
    "skills_tested": ["manage_team", "conflict_management"]
  },
  {
    "id": "PMP015",
    "domain": "business_environment",
    "knowledge_area": "stakeholder-management",
    "process_group": "planning",
    "difficulty": "easy",
    "question_type": "multiple_choice",
    "scenario": "During project initiation, the project manager is identifying individuals and groups who may affect or be affected by the project.",
    "question": "Which document is the PRIMARY output of the Identify Stakeholders process?",
    "options": [
      {"id": "A", "text": "Stakeholder Register"},
      {"id": "B", "text": "Stakeholder Engagement Plan"},
      {"id": "C", "text": "Communications Management Plan"},
      {"id": "D", "text": "Risk Register"}
    ],
    "correct_answer": "A",
    "explanation": "The Stakeholder Register is the primary output of the Identify Stakeholders process. It contains information about identified stakeholders including their interests, influence, and impact. The Stakeholder Engagement Plan (B) is an output of Plan Stakeholder Engagement. The Communications Management Plan (C) is a subsidiary plan. The Risk Register (D) is an output of Identify Risks.",
    "references": ["PMBOK 6th Ed, Section 13.1"],
    "skills_tested": ["identify_stakeholders"]
  }
]

