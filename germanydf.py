import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Rayansh\OneDrive\Desktop\ico\germany\germanydf.csv")
df = df[1:].copy()
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

latest_year = df['Year'].max()
df_latest = df[df['Year'] == latest_year]
df_latest = df_latest[df_latest['Value'] > 0]

indicator_summary = df_latest.groupby('Indicator Name')['Value'].sum()
top_n = 10
top_indicators = indicator_summary.sort_values(ascending=False)[:top_n]

agri_df = df[df['Indicator Name'] == "Agricultural land (sq. km)"]
agri_df = agri_df.dropna(subset=['Year', 'Value'])
agri_df = agri_df.sort_values('Year')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

labels = [name[:30] + '...' if len(name) > 30 else name for name in top_indicators.index]
wedges, texts, autotexts = ax1.pie(top_indicators, labels=labels, autopct='%1.1f%%',
                                   wedgeprops=dict(width=0.3), startangle=140,
                                   textprops={'fontsize': 9})

ax1.axis('equal')
ax1.set_title('Top 10 Indicator Shares')

ax2.bar(agri_df['Year'], agri_df['Value'], color='seagreen')
ax2.set_xlabel('Year')
ax2.set_ylabel('Area (sq. km)')
ax2.set_title('Agricultural Land Area in Germany')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
