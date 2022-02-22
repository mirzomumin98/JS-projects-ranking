import requests

from plotly.graph_objs import Bar, Layout
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
response = requests.get(url, headers=headers)

response_dicts = response.json()
repos_dicts = response_dicts['items']

repos_links, stars, labels = [], [], []
for repos_dict in repos_dicts:
	stars.append(repos_dict['stargazers_count'])

	owner = repos_dict['owner']['login']
	description = repos_dict['description']
	label = f'{owner}<br />{description}'
	labels.append(label)

	repo_name = repos_dict['name']
	repo_url = repos_dict['html_url']
	repos_link = f'<a href="{repo_url}">{repo_name}</a>'
	repos_links.append(repos_link)


data = [{
	'type': 'bar',
	'x': repos_links,
	'y': stars,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(255, 128, 0)',
		'line': {'width': 1.5, 'color': 'rgb(255, 79, 0)'}
	},
	'opacity': 0.8,
}]

my_layout = {
	'title': 'Most-Starred JavaScript Projects in GitHub',
	'titlefont': {'size': 28, 'color': 'rgb(255, 128, 0)'},
	'title_x': 0.5,
	'xaxis': {
		'title': 'Repository',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Stars',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='js_repos.html')