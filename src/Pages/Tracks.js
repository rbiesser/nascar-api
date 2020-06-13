import React from 'react'
import { Container, Header, Card } from 'semantic-ui-react'
import Async from 'react-async';

const loadTracks = () =>
	fetch("https://www.nascar.com/json/tracks/")
		.then(res => (res.ok ? res : Promise.reject(res)))
		.then(res => res.json())

export default function Tracks() {
	return (
		<Container>
			<Async promiseFn={loadTracks}>
				{({ data, err, isLoading }) => {
					if (isLoading) return "Loading..."
					if (err) return `Something went wrong: ${err.message}`

					if (data)
						return (
							<div>
								<div>
									<Header as='h1' content='Tracks' />
								</div>
								<Card.Group itemsPerRow={5} doubling>
									{data.items.map(track => (
										<Card
											href={track.track_url}
											// image={driver.Image}
											header={track.track_name}
											meta={`Year Built: ${track.year_built}`}
											description={`${track.city}, ${track.state}`}
											extra={track.track_type}
										/>
									))}
								</Card.Group>
							</div>
						)
				}}
			</Async>
		</Container>
	)
}