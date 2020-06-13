import React from 'react'
import { Container, Item } from 'semantic-ui-react'
import Async from 'react-async';

const loadArticles = () =>
	fetch("https://www.nascar.com/cacher/2020/1/race_list_basic.json")
		.then(res => (res.ok ? res : Promise.reject(res)))
		.then(res => res.json())

export default function Standings() {
	return (
		<Container>
			<Async promiseFn={loadArticles}>
				{({ data, err, isLoading }) => {
					if (isLoading) return "Loading..."
					if (err) return `Something went wrong: ${err.message}`

					if (data)
						return (
							<Container style={{ padding: '1rem' }}>
								<Item.Group link divided>
									{data.map(race => (
										<Item>
											<Item.Content>
												<Item.Header as='a'>{race.race_name}</Item.Header>
												<Item.Meta>{race.track_name}</Item.Meta>
												<Item.Description content={
													`${race.number_of_cars_in_field} cars, ${race.scheduled_laps} laps
																										${race.race_comments}`
												} />
												<Item.Extra>{race.date_scheduled}</Item.Extra>
											</Item.Content>
										</Item>
									))}
								</Item.Group>
							</Container>
						)
				}}
			</Async>
		</Container>
	)
}