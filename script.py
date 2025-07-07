# Create a comprehensive cost breakdown for a $100 digital proving ground for autonomous vehicles
import pandas as pd
import numpy as np

# Define the cost breakdown based on research
cost_breakdown = {
    'Component': [
        'Cloud Computing (AWS/Azure)',
        'GPU Computing',
        'Data Storage', 
        'Unreal Engine License',
        'Simulation Software',
        'Data Transfer/Bandwidth',
        'Asset Management',
        'Security & Compliance',
        'Platform Operations',
        'Remaining Balance'
    ],
    'Cost ($)': [25.00, 18.00, 12.00, 8.00, 15.00, 7.00, 5.00, 3.00, 4.00, 3.00],
    'Percentage (%)': [25.0, 18.0, 12.0, 8.0, 15.0, 7.0, 5.0, 3.0, 4.0, 3.0],
    'Description': [
        'EC2 instances, Lambda functions, API Gateway',
        'P3/G4 instances for ML training and inference',
        'S3 storage for simulation data and assets',
        'Unreal Engine subscription for simulation',
        'Specialized AV simulation tools and licenses',
        'Data ingress/egress and CDN costs',
        'Asset versioning and management systems',
        'Security monitoring and compliance tools',
        'Load balancing, monitoring, logging',
        'Buffer for unexpected costs and scaling'
    ]
}

# Create DataFrame
df = pd.DataFrame(cost_breakdown)
print("Digital Proving Ground Cost Breakdown for $100")
print("=" * 60)
print(df.to_string(index=False))
print(f"\nTotal: ${df['Cost ($)'].sum():.2f}")

# Create a more detailed breakdown by service category
detailed_breakdown = {
    'Service Category': [
        'Infrastructure (Compute)',
        'Infrastructure (Storage)',
        'Infrastructure (Networking)',
        'Software Licensing',
        'Data Processing',
        'Security & Compliance',
        'Operations & Monitoring',
        'Buffer'
    ],
    'Services Included': [
        'AWS EC2, Lambda, Fargate',
        'S3, EBS, Data Lake',
        'VPC, Load Balancers, CDN',
        'Unreal Engine, Simulation Tools',
        'GPU Computing, ML Training',
        'WAF, Security Hub, Compliance',
        'CloudWatch, CloudTrail, Support',
        'Reserved for scaling/overages'
    ],
    'Cost ($)': [25.00, 12.00, 7.00, 23.00, 18.00, 3.00, 4.00, 8.00],
    'Percentage (%)': [25.0, 12.0, 7.0, 23.0, 18.0, 3.0, 4.0, 8.0]
}

df_detailed = pd.DataFrame(detailed_breakdown)
print("\n\nDetailed Service Category Breakdown")
print("=" * 50)
print(df_detailed.to_string(index=False))
print(f"\nTotal: ${df_detailed['Cost ($)'].sum():.2f}")

# Save to CSV for use in the app
df.to_csv('proving_ground_costs.csv', index=False)
df_detailed.to_csv('detailed_service_costs.csv', index=False)

print("\n\nCSV files created for app generation")