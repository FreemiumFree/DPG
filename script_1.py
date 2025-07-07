# Create additional cost scenarios and considerations for the app
import pandas as pd
import numpy as np

# Cost scaling scenarios
scaling_scenarios = {
    'Scenario': [
        'Light Usage (10 hours/month)',
        'Medium Usage (50 hours/month)', 
        'Heavy Usage (200 hours/month)',
        'Enterprise Usage (500 hours/month)',
        'Continuous Usage (720 hours/month)'
    ],
    'Monthly Cost ($)': [100, 350, 1200, 2800, 4500],
    'Hourly Rate ($)': [10.00, 7.00, 6.00, 5.60, 6.25],
    'Primary Cost Driver': [
        'GPU compute and licensing',
        'Balanced compute and storage',
        'Heavy GPU and data processing',
        'Enterprise licensing and support',
        'Infrastructure and data transfer'
    ]
}

df_scaling = pd.DataFrame(scaling_scenarios)
print("Cost Scaling Scenarios")
print("=" * 40)
print(df_scaling.to_string(index=False))

# Additional considerations not captured in the basic $100 breakdown
additional_considerations = {
    'Consideration': [
        'Data Ingress from Vehicles',
        'Machine Learning Model Training',
        'Multi-Region Deployment',
        'High Availability & Disaster Recovery',
        'Compliance & Audit Requirements',
        'Third-Party API Integrations',
        'Custom Development & Maintenance',
        'User Training & Support',
        'Simulation Asset Licensing',
        'Performance Optimization'
    ],
    'Potential Additional Cost ($)': [50, 200, 150, 100, 75, 25, 300, 50, 100, 75],
    'Description': [
        'Real-time data streaming from test vehicles',
        'Training AI models for autonomous driving',
        'Global deployment for reduced latency',
        'Backup systems and failover mechanisms',
        'Meeting automotive industry regulations',
        'Integration with vehicle systems and sensors',
        'Custom feature development and updates',
        'Training materials and support staff',
        'High-fidelity 3D models and environments',
        'Performance tuning and optimization services'
    ]
}

df_additional = pd.DataFrame(additional_considerations)
print("\n\nAdditional Considerations Beyond Base $100")
print("=" * 50)
print(df_additional.to_string(index=False))

# Component-specific cost variables
cost_variables = {
    'Component': [
        'Compute (EC2)',
        'GPU (P3/G4)',
        'Storage (S3)',
        'Bandwidth',
        'Licensing',
        'Operations'
    ],
    'Unit': [
        'per hour',
        'per hour',
        'per GB/month',
        'per GB transferred',
        'per user/month',
        'per month'
    ],
    'Low Cost ($)': [0.10, 0.90, 0.023, 0.09, 20, 50],
    'High Cost ($)': [3.00, 24.00, 0.15, 0.15, 500, 200],
    'Typical Cost ($)': [0.50, 8.00, 0.05, 0.12, 100, 100]
}

df_variables = pd.DataFrame(cost_variables)
print("\n\nCost Variables by Component")
print("=" * 35)
print(df_variables.to_string(index=False))

# Save all data for the app
df_scaling.to_csv('scaling_scenarios.csv', index=False)
df_additional.to_csv('additional_considerations.csv', index=False)
df_variables.to_csv('cost_variables.csv', index=False)

print("\n\nAll CSV files created for comprehensive app generation")