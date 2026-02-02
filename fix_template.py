import os

# Define the target path
file_path = os.path.join(os.getcwd(), 'hostel', 'templates', 'authority_dashboard_final.html')

# The corrected content
content = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Authority Dashboard | HMS</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            margin: 0;
            background: #f8fafc;
            font-family: "Segoe UI", sans-serif;
            display: flex;
            height: 100vh;
        }

        .sidebar {
            width: 260px;
            background: #0f172a;
            color: white;
            display: flex;
            flex-direction: column;
            padding: 20px;
            box-shadow: 4px 0 15px rgba(0, 0, 0, 0.1);
        }

        .sidebar h2 {
            margin: 0 0 40px 0;
            font-size: 22px;
            display: flex;
            align-items: center;
            gap: 12px;
            color: #38bdf8;
        }

        .nav-item {
            padding: 14px 18px;
            margin-bottom: 8px;
            cursor: pointer;
            border-radius: 10px;
            display: flex;
            align-items: center;
            gap: 12px;
            color: #94a3b8;
            transition: all 0.3s;
            font-weight: 500;
        }

        .nav-item:hover,
        .nav-item.active {
            background: #38bdf8;
            color: #0f172a;
            transform: translateX(5px);
        }

        .sidebar-footer {
            margin-top: auto;
        }

        .logout-btn {
            display: flex;
            align-items: center;
            gap: 10px;
            color: #ef4444;
            text-decoration: none;
            padding: 12px 15px;
            border-radius: 8px;
            transition: background 0.2s;
        }

        .logout-btn:hover {
            background: rgba(239, 68, 68, 0.1);
        }

        .main-content {
            flex: 1;
            padding: 40px;
            overflow-y: auto;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
        }

        .header h1 {
            color: #1e293b;
            margin: 0;
            font-size: 28px;
        }

        .header p {
            color: #64748b;
            margin: 5px 0 0 0;
        }

        .section {
            display: none;
            animation: fadeIn 0.4s ease-out;
        }

        .section.active {
            display: block;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .stat-card {
            background: white;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            gap: 20px;
            transition: transform 0.2s;
        }

        .stat-card:hover {
            transform: translateY(-5px);
        }

        .stat-icon {
            width: 60px;
            height: 60px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
        }

        .stat-info h3 {
            margin: 0;
            color: #64748b;
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .stat-info p {
            margin: 5px 0 0 0;
            font-size: 36px;
            font-weight: 800;
            color: #0f172a;
        }

        .table-container {
            background: white;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            overflow-x: auto;
        }

        .table-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
        }

        .table-header h3 {
            margin: 0;
            color: #1e293b;
            font-size: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th,
        td {
            padding: 18px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
            font-size: 15px;
        }

        th {
            color: #64748b;
            font-weight: 700;
            background: #f8fafc;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        tr:hover {
            background: #f8fafc;
        }

        .badge {
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 700;
            display: inline-block;
        }

        .badge-Pending {
            background: #fef9c3;
            color: #a16207;
        }

        .badge-Solved,
        .badge-Approved {
            background: #dcfce7;
            color: #15803d;
        }

        .badge-Rejected {
            background: #fee2e2;
            color: #b91c1c;
        }

        .action-btn {
            padding: 8px 16px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            font-size: 13px;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            margin-right: 5px;
            transition: opacity 0.2s;
        }

        .action-btn:hover {
            opacity: 0.9;
        }

        .btn-green {
            background: #22c55e;
            color: white;
        }

        .btn-red {
            background: #ef4444;
            color: white;
        }

        .hostel-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 25px;
        }

        .hostel-card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        .hostel-header {
            background: #0f172a;
            color: white;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .hostel-header h3 {
            margin: 0;
            font-size: 18px;
        }

        .room-list {
            max-height: 300px;
            overflow-y: auto;
            padding: 0;
            margin: 0;
            list-style: none;
        }

        .room-item {
            padding: 15px 20px;
            border-bottom: 1px solid #e2e8f0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .room-item:last-child {
            border-bottom: none;
        }

        .room-occupied {
            border-left: 4px solid #ef4444;
        }

        .room-vacant {
            border-left: 4px solid #22c55e;
        }

        .occupant-name {
            color: #64748b;
            font-size: 13px;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Predictive Components Styles */
        .insight-card {
            background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
            border-left: 5px solid #38bdf8;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            margin-bottom: 25px;
        }

        .insight-card.critical {
            border-left-color: #ef4444;
            background: #fffafa;
            animation: pulse-border 2s infinite;
        }

        @keyframes pulse-border {
            0% {
                border-left-color: #ef4444;
            }

            50% {
                border-left-color: #fee2e2;
            }

            100% {
                border-left-color: #ef4444;
            }
        }

        .prediction-stat {
            font-size: 24px;
            font-weight: 800;
            color: #0f172a;
            margin: 10px 0;
        }

        .prediction-badge {
            background: #e0f2fe;
            color: #0284c7;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
        }

        .alert-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 15px;
            background: white;
            border-radius: 12px;
            margin-bottom: 10px;
            border: 1px solid #e2e8f0;
        }

        .alert-icon {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
        }
    </style>
</head>

<body>
    <div class="sidebar">
        <h2><i class="fa-solid fa-user-shield"></i> HMS Authority</h2>
        <div class="nav-item active" onclick="showSection('dashboard')"><i class="fa-solid fa-chart-line"></i> Dashboard
        </div>
        <div class="nav-item" onclick="showSection('students')"><i class="fa-solid fa-users"></i> Students</div>
        <div class="nav-item" onclick="showSection('hostels')"><i class="fa-solid fa-building"></i> Hostels</div>
        <div class="nav-item" onclick="showSection('complaints')"><i class="fa-solid fa-triangle-exclamation"></i>
            Complaints</div>
        <div class="nav-item" onclick="showSection('leaves')"><i class="fa-solid fa-person-walking-luggage"></i> Leaves
        </div>
        <a href="{% url 'authority_in_out_status' %}" class="nav-item" style="text-decoration: none;"><i
                class="fa-solid fa-door-open"></i> In/Out Status</a>
        <div class="nav-item" onclick="showSection('insights')"
            style="color: #38bdf8; border: 1px dashed #38bdf8; margin-top: 10px;">
            <i class="fa-solid fa-wand-magic-sparkles"></i> AI Insights
        </div>
        <div class="sidebar-footer">
            <a href="{% url 'logout' %}" class="logout-btn"><i class="fa-solid fa-right-from-bracket"></i> Logout</a>
        </div>
    </div>

    <div class="main-content">
        {% if messages %}
        <div style="margin-bottom: 20px;">
            {% for message in messages %}
            <div
                style="padding: 15px; border-radius: 8px; margin-bottom: 10px; background: {% if message.tags == 'success' %}#dcfce7{% else %}#fee2e2{% endif %}; color: {% if message.tags == 'success' %}#166534{% else %}#991b1b{% endif %}; border: 1px solid {% if message.tags == 'success' %}#bbf7d0{% else %}#fecaca{% endif %};">
                {{ message }}
            </div>
            {% endfor %}
        </div>
        {% endif %}
        <div class="header">
            <div>
                <h1>Overview</h1>
                <p>Welcome back, {{ authority.user.username }}</p>
            </div>
            <div>
                <span style="color: #64748b; font-size: 14px;">{{ now|date:"l, F d, Y" }}</span>
            </div>
        </div>

        <div id="dashboard" class="section active">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-icon" style="background: #e0f2fe; color: #0284c7;"><i
                            class="fa-solid fa-users"></i></div>
                    <div class="stat-info">
                        <h3>Total Students</h3>
                        <p>{{ stats.total_students }}</p>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon" style="background: #fef3c7; color: #d97706;"><i
                            class="fa-solid fa-clipboard-question"></i></div>
                    <div class="stat-info">
                        <h3>Pending Complaints</h3>
                        <p>{{ stats.pending_complaints }}</p>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon" style="background: #fee2e2; color: #be123c;"><i
                            class="fa-solid fa-envelope-open-text"></i></div>
                    <div class="stat-info">
                        <h3>Pending Leaves</h3>
                        <p>{{ stats.pending_leaves }}</p>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon" style="background: #dcfce7; color: #16a34a;"><i class="fa-solid fa-bed"></i>
                    </div>
                    <div class="stat-info">
                        <h3>Occupancy</h3>
                        <p>{{ stats.occupied_rooms }}/{{ stats.total_rooms }}</p>
                    </div>
                </div>
            </div>

            <!-- Dashboard Charts -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-bottom: 40px;">
                <div class="table-container">
                    <div class="table-header">
                        <h3><i class="fa-solid fa-pie-chart me-2"></i>Complaint Distribution</h3>
                    </div>
                    <div style="height: 250px; position: relative;">
                        <canvas id="complaintChart"></canvas>
                    </div>
                </div>
                <div class="table-container">
                    <div class="table-header">
                        <h3><i class="fa-solid fa-chart-bar me-2"></i>Leave Status</h3>
                    </div>
                    <div style="height: 250px; position: relative;">
                        <canvas id="leaveChart"></canvas>
                    </div>
                </div>
            </div>

            <div class="table-container">
                <div class="table-header">
                    <h3>Recent Complaints</h3>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Student</th>
                            <th>Issue</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for c in complaints|slice:":5" %}
                        <tr>
                            <td>{{ c.complaint_date|date:"M d" }}</td>
                            <td>{{ c.student.first_name }} ({{ c.student.usn }})</td>
                            <td>{{ c.facility.name }}</td>
                            <td><span class="badge badge-{{ c.status }}">{{ c.status }}</span></td>
                        </tr>
                        {% empty %}
                        <tr>
                            <td colspan="4">No recent complaints.</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>

        <div id="students" class="section">
            <div class="table-container">
                <div class="table-header">
                    <h3>Registered Students</h3>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>USN</th>
                            <th>Name</th>
                            <th>Room</th>
                            <th>Hostel</th>
                            <th>Contact</th>
                            <th>Details</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for s in students %}
                        <tr>
                            <td style="font-weight: 600;">{{ s.usn }}</td>
                            <td>{{ s.first_name }} {{ s.last_name }}</td>
                            <td>{{ s.room.room_number }}</td>
                            <td>{{ s.room.hostel.hostel_name }}</td>
                            <td>{{ s.phone }}</td>
                            <td>
                                <a href="{% url 'authority_student_detail' s.id %}" class="action-btn"
                                    style="background: #3b82f6; color: white;">
                                    <i class="fa-solid fa-eye"></i> View
                                </a>
                            </td>
                        </tr>
                        {% empty %}
                        <tr>
                            <td colspan="6">No students registered.</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>

        <div id="hostels" class="section">
            <div class="hostel-grid">
                {% for hostel in hostels %}
                <div class="hostel-card">
                    <div class="hostel-header">
                        <h3>{{ hostel.hostel_name }}</h3>
                        <span>
                            <i class="fa-solid fa-location-dot"></i> Block {{ hostel.block_number|default:"A" }}
                        </span>
                    </div>
                    <ul class="room-list">
                        {% for room in hostel.room_set.all %}
                        <li class="room-item {% if room.is_vacant %}room-vacant{% else %}room-occupied{% endif %}">
                            <div><strong>Room {{ room.room_number }}</strong> <span
                                    style="font-size: 12px; color: #64748b;">({{ room.room_type }})</span></div>
                            {% if not room.is_vacant %}
                            {% with occupant=room.student_set.first %}
                            <div class="occupant-name">{{ occupant.first_name }}</div>
                            {% endwith %}
                            {% else %}
                            <div class="occupant-name" style="color: #22c55e;">Vacant</div>
                            {% endif %}
                        </li>
                        {% endfor %}
                    </ul>
                </div>
                {% empty %}
                <p>No hostels found.</p>
                {% endfor %}
            </div>
        </div>

        <div id="complaints" class="section">
            <div class="table-container">
                <div class="table-header">
                    <h3>Complaint Management</h3>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Student</th>
                            <th>Category</th>
                            <th>Description</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for c in complaints %}
                        <tr>
                            <td>{{ c.complaint_date|date:"M d, Y" }}</td>
                            <td>
                                <div><strong>{{ c.student.first_name }} {{ c.student.last_name }}</strong></div>
                                <div style="font-size: 12px; color: #64748b;">{{ c.student.room.hostel.hostel_name }} -
                                    {{ c.student.room.room_number }}</div>
                            </td>
                            <td>{{ c.facility.name }}</td>
                            <td style="max-width: 300px;">{{ c.description }}</td>
                            <td><span class="badge badge-{{ c.status }}">{{ c.status }}</span></td>
                            <td>
                                {% if c.status == 'Pending' %}
                                <a href="{% url 'resolve_complaint' c.id %}" class="action-btn btn-green">Solve</a>
                                {% else %}
                                <span style="color: #64748b; font-size: 13px;">{{ c.solved_date|date:"M d" }}</span>
                                {% endif %}
                            </td>
                        </tr>
                        {% empty %}
                        <tr>
                            <td colspan="6">No complaints found.</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>

        <div id="leaves" class="section">
            <div class="table-container">
                <div class="table-header">
                    <h3>Leave Request Management</h3>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>Student</th>
                            <th>Reason</th>
                            <th>From</th>
                            <th>To</th>
                            <th>Status</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for l in leaves %}
                        <tr>
                            <td>
                                <div><strong>{{ l.student.first_name }} {{ l.student.last_name }}</strong></div>
                                <div style="font-size: 12px; color: #64748b;">{{ l.student.room.hostel.hostel_name }} -
                                    {{ l.student.room.room_number }}</div>
                            </td>
                            <td>{{ l.reason }}</td>
                            <td>{{ l.start_date|date:"M d" }}</td>
                            <td>{{ l.end_date|date:"M d" }}</td>
                            <td><span class="badge badge-{{ l.approval_status }}">{{ l.approval_status }}</span></td>
                            <td>
                                {% if l.approval_status == 'Pending' %}
                                <a href="{% url 'approve_leave' l.id %}" class="action-btn btn-green">Approve</a>
                                <a href="{% url 'reject_leave' l.id %}" class="action-btn btn-red">Reject</a>
                                {% else %}
                                <span style="color: #64748b; font-size: 13px;">Processed</span>
                                {% endif %}
                            </td>
                        </tr>
                        {% empty %}
                        <tr>
                            <td colspan="6">No leave requests found.</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>

        <div id="insights" class="section">
            <div class="grid-container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                <!-- PREDICTIVE MAINTENANCE -->
                <div class="column">
                    <div class="table-header">
                        <h3><i class="fa-solid fa-screwdriver-wrench"></i> Predictive Maintenance</h3>
                    </div>
                    {% if maintenance_alerts %}
                    {% for alert in maintenance_alerts %}
                    <div class="insight-card {% if alert.level == 'CRITICAL' %}critical{% endif %}">
                        <div style="display: flex; justify-content: space-between; align-items: start;">
                            <div>
                                <h4 style="margin: 0; color: #1e293b;">{{ alert.facility }} Alert</h4>
                                <p style="margin: 5px 0; color: #64748b; font-size: 14px;">{{ alert.hostel }} Block</p>
                            </div>
                            <span
                                class="badge {% if alert.level == 'CRITICAL' %}bg-danger{% else %}bg-warning{% endif %}"
                                style="color: white;">{{ alert.level }}</span>
                        </div>
                        <p style="margin-top: 15px; font-size: 14px; color: #475569;">
                            Detected <strong>{{ alert.count }}</strong> related complaints within 24 hours. Immediate
                            inspection recommended to prevent failure.
                        </p>
                        <div style="margin-top: 15px; display: flex; gap: 10px;">
                            <a href="{% url 'trigger_maintenance_alert' %}?facility={{ alert.facility }}&hostel={{ alert.hostel }}"
                                class="action-btn btn-green" style="font-size: 12px; padding: 6px 12px;">Bypass
                                Queue</a>
                            <button class="action-btn"
                                style="background: #e2e8f0; color: #475569; font-size: 12px; padding: 6px 12px;">Ignore</button>
                        </div>
                    </div>
                    {% endfor %}
                    {% else %}
                    <div class="insight-card" style="border-left-color: #22c55e;">
                        <h4 style="margin: 0; color: #1e293b;">All Systems Clear</h4>
                        <p style="margin: 5px 0; color: #64748b; font-size: 14px;">No critical clusters detected in the
                            last 24 hours.</p>
                    </div>
                    {% endif %}
                </div>

                <!-- PREDICTIVE SUPPLY ALLOCATION -->
                <div class="column">
                    <div class="table-header">
                        <h3><i class="fa-solid fa-boxes-stacked"></i> Supply Allocation Prediction</h3>
                    </div>
                    <div class="insight-card">
                        <div style="display: flex; justify-content: space-between;">
                            <span class="prediction-badge">Upcoming Week Trend: {{ supply_prediction.trend }}</span>
                            <i class="fa-solid fa-chart-line" style="color: #64748b;"></i>
                        </div>
                        <div class="prediction-stat">{{ supply_prediction.predicted_occupancy }}</div>
                        <p style="color: #64748b; font-size: 14px; margin: 0;">Predicted Daily Student Count</p>

                        <!-- Occupancy Trend Chart -->
                        <div style="height: 180px; margin-top: 20px; position: relative;">
                            <canvas id="occupancyTrendChart"></canvas>
                        </div>

                        <div style="margin-top: 25px;">
                            <div
                                style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 8px;">
                                <span>Occupancy Reduction</span>
                                <span style="font-weight: 600; color: #ef4444;">-{{ supply_prediction.reduction_percentage }}%</span>
                            </div>
                            <div
                                style="width: 100%; height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden;">
                                <div style="width: {{ supply_prediction.reduction_percentage }}%; height: 100%; background: #ef4444;"></div>
                            </div>
                        </div>

                        <div style="margin-top: 25px; display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                            <div
                                style="background: white; padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; text-align: center;">
                                <div style="font-size: 20px; font-weight: 700;">{{ supply_prediction.predicted_absent }}</div>
                                <div style="font-size: 11px; color: #64748b; text-transform: uppercase;">Expected Absent
                                </div>
                            </div>
                            <div
                                style="background: white; padding: 15px; border-radius: 12px; border: 1px solid #e2e8f0; text-align: center;">
                                <div style="font-size: 20px; font-weight: 700; color: #22c55e;">{{ supply_prediction.trend }}</div>
                                <div style="font-size: 11px; color: #64748b; text-transform: uppercase;">Budget Outlook
                                </div>
                            </div>
                        </div>

                        <div
                            style="margin-top: 25px; padding: 15px; background: #fffbeb; border-radius: 12px; border-left: 4px solid #f59e0b;">
                            <p style="margin: 0; font-size: 13px; color: #92400e;">
                                <strong>Smart Recommendation:</strong> Reduce perishable supply orders by {{ supply_prediction.reduction_percentage }}% to minimize waste.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script>
        function showSection(sectionId) {
            document.querySelectorAll('.section').forEach(el => el.classList.remove('active'));
            document.getElementById(sectionId).classList.add('active');
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            if (event) event.currentTarget.classList.add('active');
            const titles = { 'dashboard': 'Overview', 'students': 'Student Directory', 'hostels': 'Hostel & Room Status', 'complaints': 'Complaint Management', 'leaves': 'Leave Requests', 'insights': 'Predictive Analytics & AI Insights' };
            document.querySelector('.header h1').innerText = titles[sectionId];
        }

        // --- Charts Initialization ---
        // Complaint Chart
        const ctxComplaint = document.getElementById('complaintChart').getContext('2d');
        const complaintChart = new Chart(ctxComplaint, {
            type: 'doughnut',
            data: {
                labels: {{ complaint_chart.labels|safe }},
                datasets: [{
                    data: {{ complaint_chart.counts|safe }},
                    backgroundColor: ['#fef3c7', '#dcfce7', '#fee2e2'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });

        // Leave Chart
        const ctxLeave = document.getElementById('leaveChart').getContext('2d');
        const leaveChart = new Chart(ctxLeave, {
            type: 'bar',
            data: {
                labels: {{ leave_chart.labels|safe }},
                datasets: [{
                    label: 'Requests',
                    data: {{ leave_chart.counts|safe }},
                    backgroundColor: ['#4ade80', '#f87171', '#fbbf24'],
                    borderRadius: 5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });

        // Occupancy Trend Chart (Line Chart)
        const ctxTrend = document.getElementById('occupancyTrendChart').getContext('2d');
        const gradient = ctxTrend.createLinearGradient(0, 0, 0, 180);
        gradient.addColorStop(0, 'rgba(56, 189, 248, 0.4)');
        gradient.addColorStop(1, 'rgba(56, 189, 248, 0)');

        const trendChart = new Chart(ctxTrend, {
            type: 'line',
            data: {
                labels: {{ supply_prediction.trend_labels|safe }},
                datasets: [{
                    label: 'Predicted Occupancy',
                    data: {{ supply_prediction.trend_series|safe }},
                    borderColor: '#38bdf8',
                    backgroundColor: gradient,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 4,
                    pointBackgroundColor: '#38bdf8',
                    borderWidth: 3
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: { grid: { display: false } },
                    y: {  
                        beginAtZero: false, 
                        grid: { color: '#f1f5f9' },
                         suggestedMin: 0
                    }
                }
            }
        });
    </script>
</body>

</html>
"""

try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully wrote to {file_path}")
except Exception as e:
    print(f"Error: {e}")
