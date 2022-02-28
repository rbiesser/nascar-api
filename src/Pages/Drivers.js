import React from 'react'
import { Container, Header, Card } from 'semantic-ui-react'
import Async from 'react-async';

const loadDrivers = () =>
	fetch("https://www.nascar.com/json/drivers/?category=nascar-cup-series")
		.then(res => (res.ok ? res : Promise.reject(res)))
		.then(res => res.json())

export default function Drivers() {
	return (
		<Container>
			<Async promiseFn={loadDrivers}>
				{({ data, err, isLoading }) => {
					if (isLoading) return "Loading..."
					if (err) return `Something went wrong: ${err.message}`

					if (data)
						return (
							<div>
								<div>
									<Header as='h1' content='Drivers' />
								</div>
								<Card.Group itemsPerRow={6} doubling>
									{data.response.map(driver => (
										<Card
											href={driver.Driver_Page}
											image={driver.Image}
											header={driver.Full_Name}
											meta={`Rookie Year: ${driver.Rookie_Year_Series_1}`}
											extra={`#${driver.Badge} ${driver.Team}`}
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
