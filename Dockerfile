FROM golang:1.23-alpine AS builder
RUN apk add --no-cache git build-base ca-certificates
WORKDIR /app

COPY . .

# DEBUG: This prints every file Docker actually copied so you can see what is missing
RUN echo "=== AVAILABLE FILES ===" && ls -R && echo "======================="

RUN if [ ! -f go.mod ]; then \
        go mod init credkellar/frequency && \
        go mod tidy; \
    else \
        go mod tidy; \
    fi

RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o frequency ./...

FROM alpine:3.19 AS runner
RUN apk add --no-cache ca-certificates tzdata
WORKDIR /app
COPY --from=builder /app/frequency .
ENTRYPOINT ["./frequency"]
