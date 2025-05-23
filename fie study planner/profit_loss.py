import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class ProfitLossAnalyzer:
    def __init__(self):
        self.revenue_data = {
            'Subscription Fees': [1200, 1500, 1800],
            'Premium Features': [300, 450, 600],
            'Advertising': [200, 250, 300]
        }
        
        self.cost_data = {
            'Hosting Costs': [200, 200, 200],
            'API Costs': [100, 120, 150],
            'Salaries': [3000, 3000, 3000],
            'Marketing': [500, 400, 300],
            'Software Tools': [100, 100, 100]
        }
        
        self.quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023']
    
    def generate_report(self):
        # Create DataFrames
        revenue_df = pd.DataFrame(self.revenue_data, index=self.quarters)
        cost_df = pd.DataFrame(self.cost_data, index=self.quarters)
        
        # Calculate totals
        revenue_df['Total Revenue'] = revenue_df.sum(axis=1)
        cost_df['Total Costs'] = cost_df.sum(axis=1)
        
        # Calculate profit
        profit_df = pd.DataFrame({
            'Total Revenue': revenue_df['Total Revenue'],
            'Total Costs': cost_df['Total Costs'],
            'Net Profit': revenue_df['Total Revenue'] - cost_df['Total Costs']
        })
        
        # Generate visualization
        plt.figure(figsize=(10, 6))
        profit_df[['Total Revenue', 'Total Costs', 'Net Profit']].plot(kind='bar')
        plt.title('Profit & Loss Statement')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('profit_loss_chart.png')
        
        # Save to Excel
        with pd.ExcelWriter('profit_loss_summary.xlsx') as writer:
            revenue_df.to_excel(writer, sheet_name='Revenue')
            cost_df.to_excel(writer, sheet_name='Costs')
            profit_df.to_excel(writer, sheet_name='Profit Analysis')
        
        print("P&L report generated: profit_loss_summary.xlsx")
        print("Chart saved: profit_loss_chart.png")

if __name__ == "__main__":
    analyzer = ProfitLossAnalyzer()
    analyzer.generate_report()