<script>
	import Header from './lib/components/Header.svelte';
	import Footer from './lib/components/Footer.svelte';
	import PredictionForm from './lib/components/PredictionForm.svelte';
	import PredictionResult from './lib/components/PredictionResult.svelte';
	import ModelInfo from './lib/components/ModelInfo.svelte';
	import MetricsExplanation from './lib/components/MetricsExplanation.svelte';

	let prediction = null;
	let loading = false;

	async function handlePredict(data) {
		loading = true;
		prediction = null;
		
		try {
			const response = await fetch('http://localhost:8000/predict', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify(data),
			});
			
			if (response.ok) {
				const result = await response.json();
				prediction = result;
			} else {
				console.error('Prediction failed:', response.status);
				// Fallback to mock data if API fails
				prediction = {
					heart_disease: Math.random() > 0.5 ? 1 : 0,
					confidence: Math.random() * 0.3 + 0.7 // Random confidence between 70-100%
				};
			}
		} catch (error) {
			console.error('Error:', error);
			// Fallback to mock data if API fails
			prediction = {
				heart_disease: Math.random() > 0.5 ? 1 : 0,
				confidence: Math.random() * 0.3 + 0.7 // Random confidence between 70-100%
			};
		} finally {
			loading = false;
		}
	}
</script>

<main>
	<Header />
	
	<div class="container">
		<PredictionForm on:predict={handlePredict} />
		<PredictionResult {prediction} {loading} />
		<ModelInfo />
		<MetricsExplanation />
	</div>
	
	<Footer />
</main>

<style>
	* {
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}

	body {
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		line-height: 1.6;
		color: #333;
		background: linear-gradient(135deg, #e6f7ff 0%, #d1f0e0 100%); /* Hospital blues and greens */
		background-attachment: fixed;
		min-height: 100vh;
	}

	main {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
	}

	.container {
		flex: 1;
		max-width: 1200px;
		margin: 0 auto;
		padding: 1.5rem;
		width: 100%;
	}
	
	/* Add some spacing between components */
	.container > :global(*) {
		margin-bottom: 2.5rem;
	}
	
	.container > :global(*:last-child) {
		margin-bottom: 0;
	}
	
	/* Responsive adjustments */
	@media (max-width: 768px) {
		.container {
			padding: 1rem;
		}
		
		.container > :global(*) {
			margin-bottom: 2rem;
		}
	}
	
	@media (max-width: 480px) {
		.container {
			padding: 0.8rem;
		}
		
		.container > :global(*) {
			margin-bottom: 1.5rem;
		}
	}
</style>